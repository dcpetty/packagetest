# __main__.py

import logging
FORMAT = '%(levelname)s:%(name)20s:%(message)s'
logging.basicConfig(format=FORMAT, level='INFO')
logger = logging.getLogger(__name__)
logger.info(f" \u2191 __main__.py (__package__={repr(__package__)})")

# From https://stackoverflow.com/a/65780624/17467335 to fix relative imports.
from sys import path
from pathlib import Path
from collections import OrderedDict
logger.debug(str(Path(__file__).resolve().parents[0]))   # up to the package
path.insert(1, str(Path(__file__).resolve().parents[0]))
path = list(OrderedDict.fromkeys(path))
logger.debug(path)

__version__ = '0.0.1'   # must be first, since a imports __main__

from package import a, b, c
logger.info(f"   a.a={repr(a.a)}")
logger.info(f"   b.b={repr(b.b)}")
logger.info(f"   c.c={repr(c.c)}")

import d
logger.info(f"   d.d={repr(d.d)}")
