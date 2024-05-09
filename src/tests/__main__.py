# test.__main__.py

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
_logger.debug(str(_P(__file__).resolve().parents[1]))  # up to the package
_p.insert(1, str(_P(__file__).resolve().parents[1]))
_p = list(_OD.fromkeys(_p))
_logger.debug(_p)

import unittest

# import test modules.
from tests import *
_logger.info(f"   after from tests import *({dir()})")


def run_tests(verbosity=2):
    """Run all tests in test_paths."""

    # initialize the test suite
    loader = unittest.TestLoader()
    suite  = unittest.TestSuite()

    # add tests to the test suite
    suite.addTests(loader.loadTestsFromModule(ta))
    suite.addTests(loader.loadTestsFromModule(tb))
    suite.addTests(loader.loadTestsFromModule(tc))
    suite.addTests(loader.loadTestsFromModule(td))

    # initialize a runner, pass it your suite and run it
    runner = unittest.TextTestRunner(verbosity=verbosity)
    result = runner.run(suite)

if __name__ == '__main__':
    _logger.info(f"prior to run_tests()")
    run_tests()
