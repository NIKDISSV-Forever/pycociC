from __future__ import annotations

from argparse import ArgumentParser
from logging import warning

from psutil import disk_partitions

from pycociC import *


def main():
    if not dont_write_bytecode():
        warning('pycociC doesn\'t remove bytecode files.\n'
                '\tYou can use "-B" option of python or PYTHONDONTWRITEBYTECODE=x to do so.\n\n')

    disks = *(disk.device for disk in disk_partitions(all=True)),

    arg_parser = ArgumentParser('pycociC', description='pycociC - A tool to remove pycache (and numba cache) files')
    arg_parser.add_argument('-t', '-d', '--dirs', nargs='+',
                            help=f'Directories to search for pycache files (default: {disks})')
    args = arg_parser.parse_args()

    eat_cache(args.dirs or disks)


if __name__ == '__main__':
    main()
