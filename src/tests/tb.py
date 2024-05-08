# tb.py

import logging as _logging
FORMAT = '%(levelname)s:%(name)10s:%(message)s'
_logging.basicConfig(format=FORMAT, level='INFO')
_logger = _logging.getLogger(__name__)
_logger.info(f" \u2191 tb.py (__package__={repr(__package__)})")

import unittest
from . import b

class TestB(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_b(self):
        _logger.info(f"   test_b()")
        self.assertEqual('b', b.b)
