# mod.pkg.d.py

import logging as _logging
FORMAT = '%(levelname)s:%(name)10s:%(message)s'
_logging.basicConfig(format=FORMAT, level='INFO')
_logger = _logging.getLogger(__name__)
_logger.info(f" \u2191 d.py (__package__={repr(__package__)})")

d = 'd'

from .. import *
_logger.info(f"   dir()={repr(dir())})")

def func():
    _logger.info(f"   [a.a, b.b, c.c, d, ]={repr([a.a, b.b, c.c, d, ])})")
