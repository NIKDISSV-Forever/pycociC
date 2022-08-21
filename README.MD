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
FP_RE = re.compile(r'.*\.py([co]|.*\.nb[ci])', re.I)


def eat_cache(at_dirs: Iterable[AnyStr, os.PathLike[AnyStr]] = ('.',)):
    """Function removes files matching the regular expression (see FP_RE) from all "__pycache__" folders recursively."""
    ...


def dont_write_bytecode() -> bool:
    """return True if env PYTHONDONTWRITEBYTECODE or -B arg passed else False"""
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
