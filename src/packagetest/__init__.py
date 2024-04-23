# __init__.py

import logging
FORMAT = '%(levelname)s:%(name)11s:%(message)s'
logging.basicConfig(format=FORMAT, level='INFO')
logger = logging.getLogger(__name__)
logger.info(f" \u2191 __init__.py")

import collections
import os
import shlex
import sys

# Update sys.path and remove duplicate entries.
sys.path.insert(1, os.path.dirname(os.path.realpath(__file__)))
unique_path = list(collections.OrderedDict.fromkeys(sys.path))
logger.debug(f"sys.path:\n{repr(sys.path)}\n{repr(unique_path)}")
sys.path = unique_path

import bar
import baz

__version__ = '0.0.1'


def main(argv):
    """Echo argv."""
    logger.info(f"   main({repr(shlex.join(argv))})")
    logger.info(f" \u2192 bar.bar({repr('MAIN')})")
    bar.bar('MAIN')

if __name__ == '__main__':
    # Check whether imported in an IDE.
    is_idle, is_pycharm, is_jupyter = (
        'idlelib' in sys.modules,
        int(os.getenv('PYCHARM', 0)),
        '__file__' not in globals()
    )
    if any((is_idle, is_pycharm, is_jupyter,)):
        tests = [
            [ 'packagetest.py', '-?', ],
        ]
        for test in tests:
            main(test)
    else:
        sys.exit(main(sys.argv))
