# test.__init__.py

import logging as _logging
FORMAT = '%(levelname)s:%(name)10s:%(message)s'
_logging.basicConfig(format=FORMAT, level='INFO')
_logger = _logging.getLogger(__name__)
_logger.info(f" \u2191 __init__.py (__package__={repr(__package__)})")

from mod import *
from mod.pkg import *
_logger.info(f"   dir()={repr(dir())})")
from . import *
_logger.info(f"   dir()={repr(dir())})")

__version__ = '0.0.2'

__all__ = ['a', 'b', 'c', 'd', 'ta', 'tb', 'tc', 'td', '__version__']
