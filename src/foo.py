# foo.py

import logging
FORMAT = '%(levelname)s:%(name)11s:%(message)s'
logging.basicConfig(format=FORMAT, level='INFO')
logger = logging.getLogger(__name__)
logger.info(f" \u2191 foo.py")

import packagetest
def foo(arg):
    """Echo arg."""
    logger.info(f"   foo({repr(arg)})")
    logger.info(f" \u2192 packagetest.bar.bar({repr(arg)})")
    packagetest.bar.bar(arg)
    logger.info(f"   packagetest.__version__={repr(packagetest.__version__)}")

if __name__ == '__main__':
    foo('FOO')
