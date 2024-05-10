# mod.__main__.py

import logging as _logging
FORMAT = '%(levelname)s:%(name)10s:%(message)s'
_logging.basicConfig(format=FORMAT, level='INFO')
_logger = _logging.getLogger(__name__)
_logger.info(f" \u2191 __main__.py (__package__={repr(__package__)})")

# From https://stackoverflow.com/a/65780624/17467335 to fix relative imports.
from sys import path as _p
from pathlib import Path as _P
from collections import OrderedDict as _OD
# path hack: add package directory to path.
_logger.debug(str(_P(__file__).resolve().parents[1]))   # up to the package
_p.insert(1, str(_P(__file__).resolve().parents[1]))
_p = list(_OD.fromkeys(_p))
_logger.debug(_p)

from mod import *
from mod.pkg import *
_logger.info(f"   dir()={repr(dir())})")
_logger.info(f"   (pkg.d.d={repr(pkg.d.d)})")

import sys
for m in [ 'mod', 'mod.a', 'mod.b', 'mod.c', 'mod.pkg', 'mod.pkg.d', ]:
    del sys.modules[m]

from mod import a, b, c
from mod.pkg import d
_logger.info(f"   dir()={repr(dir())})")

if __name__ == '__main__':
    _logger.info(f" \u2192 d.func()")
    d.func()
    _logger.info(f"   EXECUTABLE (__version__={repr(__version__)})")

# Typical __main__.py:
'''
#!/usr/bin/env python3

# From https://stackoverflow.com/a/65780624/17467335 to fix relative imports.
from sys import path as _p
from pathlib import Path as _P
from collections import OrderedDict as _OD
# path hack: add package directory to path.
_p.insert(1, str(_P(__file__).resolve().parents[1]))
_p = list(_OD.fromkeys(_p))

from package import *

def main():
    """Create a main() function using symbols imported from package."""
    pass

if __name__ == '__main__':
    main()
'''