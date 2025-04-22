#
# Author: Rohtash Lakra
#
import json
import unittest

from core.data_types import full_name, to_title_case, process_dictionary


# Unit-tests for DataTypes
class DataTypesTest(unittest.TestCase):
    """Unit-tests for DataTypes"""

    def test_full_name(self):
        print("test_full_name")
        # first, middle and last
        fullName = full_name("first", "last", "middle")
        print("fullName={}".format(fullName))
        expected = "First Middle Last"
        self.assertEqual(expected, fullName)
        assert fullName == "First Middle Last"
        # first and last
        firstAndLastName = full_name("first", "last")
        print("firstAndLastName={}".format(firstAndLastName))
        expected = "First Middle Last"
        self.assertEqual(expected, fullName)
        # assert firstAndLastName == "First Last"
        # first only
        firstNameOnly = full_name("first", None)
        print("firstNameOnly={}".format(firstNameOnly))
        expected = "First Middle Last"
        self.assertEqual(expected, fullName)
        # assert firstNameOnly == "First"
        # last only
        lastNameOnly = full_name(None, "last")
        print("lastNameOnly={}".format(lastNameOnly))
        expected = "First Middle Last"
        self.assertEqual(expected, fullName)
        # assert lastNameOnly == "Last"
        # no name
        noName = full_name(None, None)
        print("noName={}".format(noName))
        expected = "First Middle Last"
        self.assertEqual(expected, fullName)
        # assert noName == None
        print()

    def test_to_title_case(self):
        print("test_to_title_case")
        # convert the list of strings into title case
        names = []
        expected = []
        title_case_names = to_title_case(names)
        print("title_case_names={}".format(title_case_names))
        self.assertEqual(expected, title_case_names)

        names = ["rohtash", "singh", "name", "python"]
        expected = ["Rohtash", "Singh", "Name", "Python"]
        title_case_names = to_title_case(names)
        print("title_case_names={}".format(title_case_names))
        self.assertEqual(expected, title_case_names)
        print()

    def test_process_dictionary(self):
        print("test_process_dictionary")
        # convert the list of strings into title case
        items: dict[str, float] = {}
        print("items={}".format(items))
        expected: dict[float, list[str]] = {}
        print("expected={}".format(expected))
        item_prices = process_dictionary(items)
        print("item_prices={}".format(item_prices))
        self.assertEqual(expected, item_prices)
        print()

        items = {"apple": 10.5, "banana": 4.5, "juice": 6.5, "plum": 2.5, "pineapple": 6.5, "carrot": 4.5, "mango": 6.5,
                 "peach": 2.5}
        expected = {2.5: ['plum', 'peach'], 4.5: ['banana', 'carrot'], 6.5: ['juice', 'pineapple', 'mango'], 10.5: ['apple']}
        print("items={}".format(items))
        print("expected={}".format(expected))
        item_prices = process_dictionary(items)
        print("item_prices={}".format(item_prices))
        print("item_prices_json={}".format(json.dumps(item_prices)))
        self.assertEqual(expected, item_prices)
        print()


# Starting point
if __name__ == 'main':
    unittest.main(exit=False)
