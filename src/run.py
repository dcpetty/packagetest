# run.py

import logging as _logging
FORMAT = '%(levelname)s:%(name)10s:%(message)s'
_logging.basicConfig(format=FORMAT, level='INFO')
_logger = _logging.getLogger(__name__)
_logger.info(f" \u2191 run.py (__package__={repr(__package__)})")

from test.__main__ import *

if __name__ == '__main__':
    run_tests()
