#
# Author: Rohtash Lakra
#
import unittest
from core import basics


# Unit-tests for constants
class BasicsTest(unittest.TestCase):
    """Unit-tests for Basics"""

    def test_basics(self):
        print("test_basics")
        self.assertTrue(basics.is_prime(7))
        print()
        print(basics.get_primes_mapping_with_ascii_lowercase())
        print()


# Starting point
if __name__ == 'main':
    unittest.main(exit=False)
