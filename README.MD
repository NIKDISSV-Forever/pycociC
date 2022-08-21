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

```
WARNING:root:pycociC doesn't remove bytecode files.
        You can use "-B" option of python or PYTHONDONTWRITEBYTECODE=x to do so.


Starting for .


pycociC\__pycache__
        __init__.cpython-310.pyc (4kB 699B)
        __main__.cpython-310.pyc (1kB 153B)
pycociC\__pycache__  # only if the folder has been deleted

venv\Lib\site-packages\_distutils_hack\__pycache__
        __init__.cpython-310.pyc (7kB 593B)
venv\Lib\site-packages\_distutils_hack\__pycache__

venv\Lib\site-packages\__pycache__
        _virtualenv.cpython-310.pyc (4kB 107B)
venv\Lib\site-packages\__pycache__


Removed 17kB 552B
```

> python -B -m pycociC

```
Starting for C:\, D:\


C:\...\Python310\Lib\collections\__pycache__
        abc.cpython-310.pyc (251B)
        __init__.cpython-310.pyc (48kB 468B)
C:\...\Python310\Lib\collections\__pycache__

C:\...\Python310\Lib\importlib\__pycache__  
        abc.cpython-310.pyc (15kB 904B)
        ...
        __init__.cpython-310.pyc (3kB 818B)
C:\...\Python310\Lib\importlib\__pycache__  

C:\...\Python310\Lib\urllib\__pycache__
        parse.cpython-310.pyc (33kB 817B)
        __init__.cpython-310.pyc (144B)
C:\...\Python310\Lib\urllib\__pycache__

        ...

D:\...\venv\Lib\site-packages\_distutils_hack\__pycache__
        __init__.cpython-310.pyc (7kB 593B)
D:\...\venv\Lib\site-packages\_distutils_hack\__pycache__

D:\...\venv\Lib\site-packages\__pycache__
        _virtualenv.cpython-310.pyc (4kB 107B)
D:\...\venv\Lib\site-packages\__pycache__


Removed 1MB 481kB 138B
```
