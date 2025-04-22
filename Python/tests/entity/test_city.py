#
# Author: Rohtash Lakra
#
from entity.city import City
from tests._abstract import AbstractTest


class CityTest(AbstractTest):
    """Unit-tests for city.py"""

    def test_city(self):
        print("test_city")
        city_json = {'country': 'England',
                     'latitude': '51.507222',
                     'longitude': '-0.1275',
                     'pos': '80,21!',
                     'xlabel': 'City of London',
                     'year': 0
                     }
        city = City.from_dict(city_json)
        print(f"city={city}")
        self.assertIsNotNone(city)
        self.assertEqual('City of London', city.name)
        self.assertEqual('England', city.country)
        self.assertEqual(51.507222, city.latitude)
        self.assertEqual(-0.1275, city.longitude)
        print()


# Starting point
if __name__ == 'main':
    CityTest().start()
