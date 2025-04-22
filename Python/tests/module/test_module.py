#
# Author: Rohtash Lakra
#
import unittest
from module.module import fact


class ModuleTest(unittest.TestCase):
    """Unit-tests for module.py"""

    def test_fact_module(self):
        print("test_fact_module")
        self.assertTrue(fact(7))
        print(fact(4))
        print()


# Starting point
if __name__ == 'main':
    unittest.main(exit=False)
