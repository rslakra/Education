#
# Author: Rohtash Lakra
#
import unittest
from module.http import HttpClient


class HttpTest(unittest.TestCase):
    """Unit-tests for module.py"""

    def test_get_request(self):
        print("test_get_request")
        http_client = HttpClient()
        response = None
        # response = http_client.get('https://swapi.dev/api/starships/9/')
        print(response)
        print()

    def test_post_request(self):
        print("test_post_request")
        http_client = HttpClient()
        response = None
        # response = http_client.post('https://httpbin.org/post', {"name": "Rohtash"})
        print(response)
        print()


# Starting point
if __name__ == 'main':
    unittest.main(exit=False)
