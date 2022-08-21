from __future__ import annotations

import ctypes
import os
import re
import sys
import threading
from functools import wraps
from pathlib import Path
from typing import AnyStr, Callable, Iterable, TypeVar

__all__ = ('FP_RE', 'bytes_to_pretty_view', 'eat_cache', 'dont_write_bytecode')
FP_RE = re.compile(r'.*\.py([co]|.*\.nb[ci])', re.I)
_T = TypeVar('_T')


def _run_with_max_recursion(func: Callable[[...], _T] | None = None, *, recursion_limit: int = 0x7F_FF_FF_FF,
                            stack_size: int = 0xFF_FF_FF_F) -> (
        Callable[[Callable[[...], _T]], Callable[[...], _T]] | Callable[[...], _T]):
    """Decorator for sys.setrecursionlimit and threading.stack_size from kwargs and start func"""

    def run_max_recursion_decorator(func: Callable[[...], _T]) -> Callable[[...], _T]:
        @wraps(func)
        def wrapper(*args, **kwargs) -> _T:
            reset_recursion_limit = sys.getrecursionlimit()
            sys.setrecursionlimit(recursion_limit)
            threading.stack_size(stack_size)
            result = None

            def return_here():
                nonlocal result
                result = func(*args, **kwargs)

            thread = threading.Thread(target=return_here)
            thread.start()
            thread.join()

            sys.setrecursionlimit(reset_recursion_limit)
            threading.stack_size()
            return result

        return wrapper

    if func is not None:
        return run_max_recursion_decorator(func)
    return run_max_recursion_decorator


def _ignore(_): pass


@_run_with_max_recursion
def eat_cache(at_dirs: Iterable[AnyStr, os.PathLike[AnyStr]] = ('.',)):
    """Function removes files matching the regular expression (see FP_RE) from all "__pycache__" folders recursively."""
    print(f"Starting for {', '.join(at_dirs)}\n\n")

    removed = 0
    for top in at_dirs:
        for (dirpath, _, filenames) in os.walk(top, onerror=_ignore):
            del _

            dirpath = Path(dirpath)
            if dirpath.name.casefold() != '__pycache__':
                continue

            print(dirpath)
            for filename in filenames:
                if FP_RE.fullmatch(filename):
                    try:
                        target = dirpath / filename
                        fp_size = target.stat().st_size
                        os.remove(target)
                        removed += fp_size
                        print(f'\t{filename} ({bytes_to_pretty_view(fp_size)})')
                    except OSError:
                        continue
            try:
                dirpath.rmdir()
                print(dirpath)
            except OSError:
                pass
            print()

    print(f'\nRemoved {bytes_to_pretty_view(removed)}')


def dont_write_bytecode() -> bool:
    """
    return True if env PYTHONDONTWRITEBYTECODE or -B arg passed else False

    >>> import os
    >>> os.environ['PYTHONDONTWRITEBYTECODE'] = 'x'
    >>> dont_write_bytecode()
    True
    >>> del os.environ['PYTHONDONTWRITEBYTECODE']  # or os.environ['PYTHONDONTWRITEBYTECODE'] = ''
    >>> dont_write_bytecode()
    False
    """
    env_flag = os.getenv('PYTHONDONTWRITEBYTECODE')
    if env_flag is not None:
        return bool(env_flag)

    argc = ctypes.c_int(0)
    argv = ctypes.POINTER(ctypes.c_wchar_p)()
    ctypes.pythonapi.Py_GetArgcArgv(ctypes.byref(argc), ctypes.byref(argv))
    for i in range(argc.value - len(sys.argv) + 1):
        if argv[i] == '-B':
            return True
    return False


def bytes_to_pretty_view(bytes_size: int | float, *, skip_zero: bool = False) -> str:
    """
    Converts the number of bytes into a pretty SI prefix.

    >>> bytes_to_pretty_view(0)
    '0B'
    >>> bytes_to_pretty_view(0, skip_zero=True)
    ''
    >>> bytes_to_pretty_view(1_000_000_24.)
    '100MB 24B'
    >>> bytes_to_pretty_view(0xFF_FF_FF_FF)
    '4GB 294MB 967kB 295B'
    >>> bytes_to_pretty_view(10**31)
    '10,000YB'
    """
    if skip_zero and not bytes_size:
        return ''

    def _form_str() -> str:
        mod = bytes_size % power
        return f"{int(bytes_size // power):,}{prefix}B{f' {bytes_to_pretty_view(mod, skip_zero=True)}' if mod else ''}"

    power = 1
    for prefix in ('', *'kMGTPEZY'):
        if (bytes_size / power) < 1000.:
            return _form_str()
        power *= 1000
    return _form_str()
