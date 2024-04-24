# d.py

import logging
FORMAT = '%(levelname)s:%(name)20s:%(message)s'
logging.basicConfig(format=FORMAT, level='INFO')
logger = logging.getLogger(__name__)
logger.info(f" \u2191 d.py (__package__={repr(__package__)})")

d = 'd'
