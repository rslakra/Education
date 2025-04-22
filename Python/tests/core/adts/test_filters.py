#
# Author: Rohtash Lakra
#
import logging

from core.adts.filters import BloomFilter
from tests._abstract import AbstractTest

# Configure app default loggers
logging.basicConfig(level=logging.DEBUG,
                    format="[%(asctime)s] [%(process)d] [%(levelname)s] [%(filename)s:%(lineno)s] - %(message)s",
                    force=True)

logger = logging.getLogger(__name__)


class FiltersTest(AbstractTest):
    """Unit-tests for Filters"""

    def test_bloom_filter(self):
        logger.debug(f"+test_bloom_filter()")
        bloomFilter = BloomFilter(1000, 0.01)

        # Add items
        bloomFilter.add("hello")
        bloomFilter.add("world")

        # Check for items
        # print("hello" in bloomFilter)  # True
        # print("world" in bloomFilter)  # True
        # print("python" in bloomFilter)  # False (possibly)

        self.assertTrue(bloomFilter.check("hello"))
        self.assertTrue(bloomFilter.check("world"))
        self.assertFalse(bloomFilter.check("python"))

        logger.debug(f"-test_bloom_filter()")
        print()


# Starting point
if __name__ == 'main':
    FiltersTest().start()
