# test.__init__.py

import logging as _logging
FORMAT = '%(levelname)s:%(name)10s:%(message)s'
_logging.basicConfig(format=FORMAT, level='INFO')
_logger = _logging.getLogger(__name__)
_logger.info(f" \u2191 __init__.py (__package__={repr(__package__)})")

# From https://stackoverflow.com/a/65780624/17467335 to fix relative imports.
from sys import path as _p
from pathlib import Path as _P
from collections import OrderedDict as _OD
_logger.debug(str(_P(__file__).resolve().parents[1]))   # up to the package
_p.insert(1, str(_P(__file__).resolve().parents[1]))
_p = list(_OD.fromkeys(_p))
_logger.debug(_p)

from mod import *
from mod.pkg import *
_logger.info(f"   dir()={repr(dir())})")
from . import *
_logger.info(f"   dir()={repr(dir())})")

__version__ = '0.0.2'

__all__ = ['a', 'b', 'c', 'd', 'ta', 'tb', 'tc', 'td', '__version__']
