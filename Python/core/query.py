#
# Author: Rohtash Lakra
#
from enum import Enum, unique, auto
from core.enums import AutoNameEnum


@unique
class QueryType(AutoNameEnum):
    """QueryType enum"""
    INSERT = auto()
    SELECT = auto()
    UPDATE = auto()


@unique
class SqlOperator(AutoNameEnum):
    """SqlOperator enum"""
    AND = auto()  # TRUE if all the conditions separated by AND is TRUE
    BETWEEN = auto()  # TRUE if the operand is within the range of comparisons
    IN = auto()  # TRUE if the operand is equal to one of a list of expressions
    LIKE = auto()  # TRUE if the operand matches a pattern
    NOT = auto()  # Displays a record if the condition(s) is NOT TRUE
    OR = auto()  # TRUE if any of the conditions separated by OR is TRUE


class DBUtils:
    """Database Utility"""

    __DELIMITER = ', '
    __SPACE = ' '

    @classmethod
    def __field_pair(cls, key):
        # key=%(key)s
        return f"{key}=%({key})s"


    @classmethod
    def __set_updated(cls, fields):
        return cls.__DELIMITER.join([fields, 'updated_at=UTC_TIMESTAMP()'])

    @classmethod
    def __set_where_clause(cls, query, clause: dict = None, sql_operator: SqlOperator = None):
        """Builds the where clause of SQL query"""
        if clause is None or len(clause) == 0:
            return query

        fields = f' {sql_operator.name} '.join([cls.__field_pair(key) for key in clause.keys()])
        if fields and len(fields) > 0:
            query = '{} WHERE {}'.format(query, fields)

        return query


    @classmethod
    def __where_clause(cls, clause: dict = None, sql_operator: SqlOperator = None):
        """Builds the where clause of SQL query"""
        query = ''
        if clause is None or len(clause) == 0:
            return query

        fields = cls.__DELIMITER.join([cls.__field_pair(key) for key in clause.keys()])
        if fields and len(fields) > 0:
            query = 'WHERE {}'.format(f' {sql_operator.name} '.join([fields]))

        return query

    @classmethod
    def build_query(cls, table: str, query_type: QueryType, query_data: dict = None, where_clause: dict = None):
        """Builds the SQL query"""
        if table is None:
            raise KeyError('table name should provide!')

        if type is None:
            raise KeyError('query type should provide!')

        if len(query_data) == 0:
            return None

        query = None
        match query_type:
            case QueryType.INSERT:
                query = " ".join([query_type.name, 'INTO', table])

            case QueryType.UPDATE:
                fields = cls.__DELIMITER.join([cls.__field_pair(key) for key in query_data.keys()])
                # append 'updated_at' with each update query
                fields = cls.__set_updated(fields)
                # build query
                query = cls.__SPACE.join([query_type.name, table, 'SET', str(fields)])
                # append where clause
                query = cls.__set_where_clause(query, where_clause, SqlOperator.AND)

            case _:
                query = " ".join([query_type.name, '*'])

        return query
