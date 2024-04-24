# __main__.py

import logging
FORMAT = '%(levelname)s:%(name)11s:%(message)s'
logging.basicConfig(format=FORMAT, level='INFO')
logger = logging.getLogger(__name__)
logger.info(f" \u2191 __main__.py (__package__={repr(__package__)})")

import os
import sys

from __init__ import main

"""Include if __name__ == '__main': code from __init__.py"""
# Check whether imported in an IDE.
is_idle, is_pycharm, is_jupyter = (
    'idlelib' in sys.modules,
    int(os.getenv('PYCHARM', 0)),
    '__file__' not in globals()
)
if any((is_idle, is_pycharm, is_jupyter,)):
    tests = [
        [ 'packagetest', '-?', ],
    ]
    for test in tests:
        main(test)
else:
    sys.exit(main(sys.argv))
