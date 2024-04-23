# baz.py

import logging
FORMAT = '%(levelname)s:%(name)11s:%(message)s'
logging.basicConfig(format=FORMAT, level='INFO')
logger = logging.getLogger(__name__)
logger.info(f" \u2191 baz.py")

import __init__

def baz(arg):
    """Echo arg."""
    logger.info(f"   baz.baz({repr(arg)})")
    logger.info(f"   __init__.__version__={repr(__init__.__version__)}")
