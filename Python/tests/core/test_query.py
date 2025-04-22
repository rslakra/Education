#
# Author: Rohtash Lakra
#
import unittest
from core.query import QueryType, DBUtils


# Unit-tests for constants
class DBUtilsTest(unittest.TestCase):
    """DBUtils Tests"""

    def test_query_type(self):
        print("test_query_type")
        query_types = str(list(QueryType))
        self.assertIsNotNone(query_types)
        expected = '[QueryType <INSERT=INSERT>, QueryType <SELECT=SELECT>, QueryType <UPDATE=UPDATE>]'
        self.assertEqual(expected, query_types)
        print()

    def test_dbutils_build_update_query(self):
        print("test_dbutils_build_update_query")
        query_data = {'name': 'Rohtash'}
        query = DBUtils.build_query('User', QueryType.UPDATE, query_data)
        self.assertIsNotNone(query)
        expected = "UPDATE User SET name=%(name)s, updated_at=UTC_TIMESTAMP()"
        print(f"query={query}")
        self.assertEqual(expected, query)
        print()

    def test_dbutils_build_update_query_with_where_clause(self):
        print("test_dbutils_build_update_query_with_where_clause")
        query_data = {'name': 'Rohtash', 'sex': 'male'}
        where_clause = {'id': 2}
        query = DBUtils.build_query('User', QueryType.UPDATE, query_data, where_clause)
        self.assertIsNotNone(query)
        expected = "UPDATE User SET name=%(name)s, sex=%(sex)s, updated_at=UTC_TIMESTAMP() WHERE id=%(id)s"
        print(f"query={query}")
        self.assertEqual(expected, query)
        print()

    def test_dbutils_build_update_query_with_where_and_clause(self):
        print("test_dbutils_build_update_query_with_where_and_clause")
        query_data = {'name': 'Rohtash', 'sex': 'male'}
        where_clause = {'id': 2, 'sex': 'female'}
        query = DBUtils.build_query('User', QueryType.UPDATE, query_data, where_clause)
        self.assertIsNotNone(query)
        expected = "UPDATE User SET name=%(name)s, sex=%(sex)s, updated_at=UTC_TIMESTAMP() WHERE id=%(id)s AND sex=%(sex)s"
        print(f"query={query}")
        self.assertEqual(expected, query)
        print()

    def test_dbutils_build_query(self):
        print("test_dbutils_build_query")
        query_data = {'name': 'Rohtash'}
        where_clause = {'id': 1}
        query = DBUtils.build_query('User', QueryType.UPDATE, query_data, where_clause)
        self.assertIsNotNone(query)
        expected = "UPDATE User SET name=%(name)s, updated_at=UTC_TIMESTAMP() WHERE id=%(id)s"
        print(f"query={query}")
        self.assertEqual(expected, query)
        print()


# Starting point
if __name__ == 'main':
    unittest.main(exit=False)
