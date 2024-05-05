# tc.py

import logging as _logging
FORMAT = '%(levelname)s:%(name)10s:%(message)s'
_logging.basicConfig(format=FORMAT, level='INFO')
_logger = _logging.getLogger(__name__)
_logger.info(f" \u2191 tc.py (__package__={repr(__package__)})")

import unittest
from . import c

class TestC(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_c(self):
        _logger.info(f"   test_c()")
        self.assertEqual('c', c.c)
