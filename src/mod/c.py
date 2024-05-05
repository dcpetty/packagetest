# mod.c.py

import logging as _logging
FORMAT = '%(levelname)s:%(name)10s:%(message)s'
_logging.basicConfig(format=FORMAT, level='INFO')
_logger = _logging.getLogger(__name__)
_logger.info(f" \u2191 c.py (__package__={repr(__package__)})")

c = 'c'
