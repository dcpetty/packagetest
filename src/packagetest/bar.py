# bar.py

import logging
FORMAT = '%(levelname)s:%(name)11s:%(message)s'
logging.basicConfig(format=FORMAT, level='INFO')
logger = logging.getLogger(__name__)
logger.info(f" \u2191 bar.py")

import baz

def bar(arg):
    """Echo arg."""
    logger.info(f"   bar.bar({repr(arg)})")
    logger.info(f" \u2192 baz.baz({repr(arg)})")
    baz.baz(arg)
