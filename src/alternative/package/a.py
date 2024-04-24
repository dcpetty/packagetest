# a.py

import logging
FORMAT = '%(levelname)s:%(name)20s:%(message)s'
logging.basicConfig(format=FORMAT, level='INFO')
logger = logging.getLogger(__name__)
logger.info(f" \u2191 a.py (__package__={repr(__package__)})")

a = 'a'

# From https://stackoverflow.com/a/65780624/17467335 to fix relative imports.
from sys import path
from pathlib import Path
from collections import OrderedDict
logger.debug(str(Path(__file__).resolve().parents[2]))   # up to the package
path.insert(1, str(Path(__file__).resolve().parents[2]))
path = list(OrderedDict.fromkeys(path))
logger.debug(path)

from alternative.__main__ import __version__
logger.info(f"   __main__.__version__={repr(__version__)}")
