# pycociC - A Python library for removing pycache and numba cache files

## Installation

> pip install [pycociC](https://pypi.org/project/pycociC/)

## Usage

> python **-B** -m pycociC [-t DIRS [DIRS ...]] [-h]

```
options:
  -h, --help            show this help message and exit
  -t DIRS [DIRS ...], -d DIRS [DIRS ...], --dirs DIRS [DIRS ...]
                        Directories to search for pycache files (default: (everywhere))
```

## Coding

```python
# pycociC/__init__.py
__all__ = ('FP_RE', 'bytes_to_pretty_view', 'eat_cache', 'dont_write_bytecode')
FP_RE = re.compile(r'.*\.py([co]|.*\.nb[ci])', re.I)


@_run_with_max_recursion
def eat_cache(at_dirs: Iterable[AnyStr, os.PathLike[AnyStr]] = ('.',)):
    """Function removes files matching the regular expression (see FP_RE) from all "__pycache__" folders recursively."""
    ...


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
    ...


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
    """
    ...

```

### Example Output

> python -m pycociC -d .

```stdout
WARNING:root:pycociC doesn't remove bytecode files.
        You can use "-B" option of python or PYTHONDONTWRITEBYTECODE=x to do so.


Starting for .


pycociC\__pycache__
        __init__.cpython-310.pyc (3.53 kB)
        __main__.cpython-310.pyc (1.15 kB)
pycociC\__pycache__  # if dir was removed only

venv\Lib\site-packages\psutil\__pycache__
        _common.cpython-310.pyc (21.95 kB)
        _compat.cpython-310.pyc (11.883 kB)
        _pswindows.cpython-310.pyc (28.902 kB)
        __init__.cpython-310.pyc (63.508 kB)
venv\Lib\site-packages\psutil\__pycache__

venv\Lib\site-packages\_distutils_hack\__pycache__
        __init__.cpython-310.pyc (7.591 kB)
venv\Lib\site-packages\_distutils_hack\__pycache__

venv\Lib\site-packages\__pycache__
        _virtualenv.cpython-310.pyc (4.105 kB)
venv\Lib\site-packages\__pycache__


Removed 142.619 kB
```

> python -B -m pycociC

```
Starting for C:\, D:\


C:\...\Python310\Lib\collections\__pycache__
        abc.cpython-310.pyc (251 bytes)
        __init__.cpython-310.pyc (48.468 kB)
C:\...\Python310\Lib\collections\__pycache__

C:\...\Python310\Lib\ctypes\__pycache__
        wintypes.cpython-310.pyc (4.871 kB)
        _endian.cpython-310.pyc (1.914 kB)
        __init__.cpython-310.pyc (15.895 kB)
C:\...\Python310\Lib\ctypes\__pycache__

        ...

D:\Documents\Projects\...\venv\Lib\site-packages\__pycache__
        _virtualenv.cpython-310.pyc (4.105 kB)
D:\Documents\Projects\...\venv\Lib\site-packages\__pycache__


Removed 3.3568 MB
```
