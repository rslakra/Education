#
# Author: Rohtash Lakra
#
import unittest


class AbstractTest(unittest.TestCase):
    """The AbstractTest is the base class for all unit-tests."""

    def start(self, exit: bool = False):
        unittest.main(exit=exit)
