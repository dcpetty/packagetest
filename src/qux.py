# qux.py

import logging
FORMAT = '%(levelname)s:%(name)20s:%(message)s'
logging.basicConfig(format=FORMAT, level='INFO')
logger = logging.getLogger(__name__)
logger.info(f" \u2191 qux.py (__package__={repr(__package__)})")

from alternative import __main__
logger.info(f"   dir(alternative.__main__)={dir(__main__)}")
logger.info(f"   __main__.a.a={repr(__main__.a.a)}")

from alternative.package import a
logger.info(f"   alternative.package.a.a={repr(a.a)}")
