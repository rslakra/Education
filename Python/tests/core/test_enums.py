#
# Author: Rohtash Lakra
#
import logging
import unittest
from datetime import date

from core.enums import BaseEnum, ColorEnum, WeekDaysEnum
from core.enums import EvenOddEnum, LogTypeEnum, HttpMethodEnum
from core.enums import NumberEnum, ShapeEnum, UniqueShapeEnum
from core.enums import OrdinalEnum, LowerCaseOrdinalEnum
from core.enums import Priority
from core.enums import StatusEnum, AutoNameEnum, AutoNameLowerCaseEnum

logger = logging.getLogger(__name__)


# Unit-tests for constants
class EnumsTest(unittest.TestCase):
    """Unit-tests for Enums"""

    def test_base_enum(self):
        print("test_base_enum")
        self.assertEqual("<enum 'BaseEnum'>", str(BaseEnum))
        self.assertEqual((), BaseEnum.names())
        self.assertEqual((), BaseEnum.values())
        text = 'name'
        print(f"{text} of_name={BaseEnum.of_name(text)}")
        self.assertEqual(None, BaseEnum.of_name(text))
        print(f"{text} of_value={BaseEnum.of_value(text)}")
        self.assertEqual(None, BaseEnum.of_value(text))
        print(f"{text} equals={BaseEnum.equals(BaseEnum, text)}")
        self.assertEqual(False, BaseEnum.equals(BaseEnum, text))
        print()

    def test_color_enum(self):
        print("test_color_enum")
        self.assertEqual("<enum 'ColorEnum'>", str(ColorEnum))
        self.assertEqual(('RED', 'GREEN', 'BLUE'), ColorEnum.names())
        self.assertEqual((1, 2, 3), ColorEnum.values())

        text = 'color'
        print(f"{text} of_name={ColorEnum.of_name(text)}")
        self.assertEqual(None, ColorEnum.of_name(text))

        text = 1
        expected = 'ColorEnum <RED=1>'
        self.assertEqual(expected, str(ColorEnum.of_value(text)))
        self.assertTrue(ColorEnum.equals(ColorEnum.RED, text))
        self.assertFalse(ColorEnum.equals(ColorEnum.GREEN, text))

        text = 'red'
        expected = 'ColorEnum <RED=1>'
        print(f"{text} of_name={WeekDaysEnum.of_name(text)}")
        self.assertEqual(expected, str(ColorEnum.of_name(text)))
        self.assertTrue(ColorEnum.equals(ColorEnum.RED, text))
        self.assertFalse(ColorEnum.equals(ColorEnum.GREEN, text))

        text = 2
        expected = 'ColorEnum <GREEN=2>'
        print(f"{text} of_value={ColorEnum.of_value(text)}")
        self.assertEqual(expected, str(ColorEnum.of_value(text)))
        self.assertTrue(ColorEnum.equals(ColorEnum.GREEN, text))
        self.assertFalse(ColorEnum.equals(ColorEnum.RGB, text))

        color = ColorEnum.RGB
        print(f"{color} is instance of {ColorEnum} = {isinstance(color, ColorEnum)}")
        self.assertTrue(isinstance(color, ColorEnum))
        print()

    def test_week_days_enum(self):
        print("test_week_days_enum")
        self.assertEqual("<enum 'WeekDaysEnum'>", str(WeekDaysEnum))
        self.assertEqual(('SUNDAY', 'MONDAY', 'TUESDAY', 'WEDNESDAY', 'THURSDAY', 'FRIDAY', 'SATURDAY'),
                         WeekDaysEnum.names())
        self.assertEqual((1, 2, 3, 4, 5, 6, 7), WeekDaysEnum.values())
        text = 'sunday'
        expected = 'WeekDaysEnum <SUNDAY=1>'
        print(f"{text} of_name={WeekDaysEnum.of_name(text)}")
        self.assertEqual(expected, str(WeekDaysEnum.of_name(text)))
        self.assertTrue(WeekDaysEnum.equals(WeekDaysEnum.SUNDAY, text))
        self.assertFalse(WeekDaysEnum.equals(WeekDaysEnum.MONDAY, text))

        text = 2
        expected = 'WeekDaysEnum <MONDAY=2>'
        print(f"{text} of_value={WeekDaysEnum.of_value(text)}")
        self.assertEqual(expected, str(WeekDaysEnum.of_value(text)))
        self.assertTrue(WeekDaysEnum.equals(WeekDaysEnum.MONDAY, text))
        self.assertFalse(WeekDaysEnum.equals(WeekDaysEnum.SUNDAY, text))

        # check isinstance of
        week_day = WeekDaysEnum.WEEKEND
        print(f"{week_day} is instance of {WeekDaysEnum} = {isinstance(week_day, WeekDaysEnum)}")
        self.assertTrue(isinstance(week_day, WeekDaysEnum))

        # print weekday from date
        print(f"Weekday={WeekDaysEnum.from_date(date.today())} for date:{date}. And today={WeekDaysEnum.today()}")
        print()

    def test_number_enum(self):
        print("test_number_enum")
        self.assertEqual("<enum 'NumberEnum'>", str(NumberEnum))
        self.assertEqual(('EVEN', 'ODD', 'PRIME'), NumberEnum.names())
        self.assertEqual((1, 2, 3), NumberEnum.values())
        text = 'prime'
        expected = 'NumberEnum <PRIME=3>'
        print(f"{text} of_name={NumberEnum.of_name(text)}")
        self.assertEqual(expected, str(NumberEnum.of_name(text)))
        self.assertTrue(NumberEnum.equals(NumberEnum.PRIME, text))
        self.assertFalse(NumberEnum.equals(NumberEnum.EVEN, text))

        text = 3
        expected = 'NumberEnum <PRIME=3>'
        print(f"{text} of_value={NumberEnum.of_value(text)}")
        self.assertEqual(expected, str(NumberEnum.of_value(text)))
        self.assertTrue(NumberEnum.equals(NumberEnum.PRIME, text))
        self.assertFalse(NumberEnum.equals(NumberEnum.EVEN, text))

        # check isinstance of
        prime = NumberEnum.PRIME
        is_prime = isinstance(prime, NumberEnum)
        print(f"{prime} is instance of {NumberEnum} = {is_prime}")
        self.assertTrue(is_prime)
        print()

    def test_shape_enum(self):
        print("test_shape_enum")
        self.assertEqual("<enum 'ShapeEnum'>", str(ShapeEnum))
        self.assertEqual(('CIRCLE', 'DIAMOND', 'SQUARE'), ShapeEnum.names())
        expected_all_shapes = "[('CIRCLE', ShapeEnum <CIRCLE=1>), ('DIAMOND', ShapeEnum <DIAMOND=2>), ('SQUARE', ShapeEnum <SQUARE=3>), ('DIAMOND_ALIAS', ShapeEnum <DIAMOND=2>)]"
        self.assertEqual(expected_all_shapes, str(ShapeEnum.all_shapes()))
        self.assertEqual((1, 2, 3), ShapeEnum.values())

        text = 'circle'
        expected = 'ShapeEnum <CIRCLE=1>'
        print(f"{text} of_name={ShapeEnum.of_name(text)}")
        self.assertEqual(expected, str(ShapeEnum.of_name(text)))
        self.assertTrue(ShapeEnum.equals(ShapeEnum.CIRCLE, text))
        self.assertFalse(ShapeEnum.equals(ShapeEnum.DIAMOND, text))

        text = 2
        expected = 'ShapeEnum <DIAMOND=2>'
        print(f"{text} of_value={ShapeEnum.of_value(text)}")
        self.assertEqual(expected, str(ShapeEnum.of_value(text)))
        self.assertTrue(ShapeEnum.equals(ShapeEnum.DIAMOND, text))
        self.assertFalse(ShapeEnum.equals(ShapeEnum.CIRCLE, text))

        # check isinstance of
        shape = ShapeEnum.CIRCLE
        is_shape = isinstance(shape, ShapeEnum)
        print(f"{shape} is instance of {ShapeEnum} = {is_shape}")
        self.assertTrue(is_shape)
        print()

    def test_unique_shape_enum(self):
        print("test_unique_shape_enum")
        self.assertEqual("<enum 'UniqueShapeEnum'>", str(UniqueShapeEnum))
        self.assertEqual(('CIRCLE', 'DIAMOND', 'SQUARE'), UniqueShapeEnum.names())
        self.assertEqual((1, 2, 3), UniqueShapeEnum.values())

        text = 'circle'
        expected = 'UniqueShapeEnum <CIRCLE=1>'
        print(f"{text} of_name={UniqueShapeEnum.of_name(text)}")
        self.assertEqual(expected, str(UniqueShapeEnum.of_name(text)))
        self.assertTrue(UniqueShapeEnum.equals(UniqueShapeEnum.CIRCLE, text))
        self.assertFalse(UniqueShapeEnum.equals(UniqueShapeEnum.DIAMOND, text))

        text = 2
        expected = 'UniqueShapeEnum <DIAMOND=2>'
        print(f"{text} of_value={UniqueShapeEnum.of_value(text)}")
        self.assertEqual(expected, str(UniqueShapeEnum.of_value(text)))
        self.assertTrue(UniqueShapeEnum.equals(UniqueShapeEnum.DIAMOND, text))
        self.assertFalse(UniqueShapeEnum.equals(UniqueShapeEnum.CIRCLE, text))

        # check isinstance of
        shape = UniqueShapeEnum.CIRCLE
        is_shape = isinstance(shape, UniqueShapeEnum)
        print(f"{shape} is instance of {UniqueShapeEnum} = {is_shape}")
        self.assertTrue(is_shape)
        print()

    def test_status_enum(self):
        print("test_status_enum")
        self.assertEqual("<enum 'StatusEnum'>", str(StatusEnum))
        self.assertEqual(('ENABLED', 'DISABLED', 'MODIFIED', 'DELETED'), StatusEnum.names())
        self.assertEqual(('enabled', 'disabled', 'modified', 'deleted'), StatusEnum.values())

        text = 'enabled'
        expected = 'StatusEnum <ENABLED=enabled>'
        print(f"{text} of_name={StatusEnum.of_name(text)}")
        self.assertEqual(expected, str(StatusEnum.of_name(text)))
        self.assertTrue(StatusEnum.equals(StatusEnum.ENABLED, text))
        self.assertFalse(StatusEnum.equals(StatusEnum.DISABLED, text))

        text = 'disabled'
        expected = 'StatusEnum <DISABLED=disabled>'
        print(f"{text} of_value={StatusEnum.of_value(text)}")
        self.assertEqual(expected, str(StatusEnum.of_value(text)))
        self.assertTrue(StatusEnum.equals(StatusEnum.DISABLED, text))
        self.assertFalse(StatusEnum.equals(StatusEnum.ENABLED, text))

        # check isinstance of
        status = StatusEnum.ENABLED
        is_enabled = isinstance(status, StatusEnum)
        print(f"{status} is instance of {StatusEnum} = {is_enabled}")
        self.assertTrue(is_enabled)
        self.assertEqual(status.value, StatusEnum.ENABLED.name.lower())
        self.assertEqual(status, StatusEnum.ENABLED)
        # Reversed
        # self.assertEqual(('SQUARE', 'DIAMOND', 'CIRCLE'), reversed(str(StatusEnum)))
        print()

    def test_auto_name_enum(self):
        print("test_auto_name_enum")
        self.assertEqual("<enum 'AutoNameEnum'>", str(AutoNameEnum))
        self.assertEqual((), AutoNameEnum.names())
        self.assertEqual((), AutoNameEnum.values())
        print()

    def test_auto_name_lower_case_enum(self):
        print("test_auto_name_lower_case_enum")
        self.assertEqual("<enum 'AutoNameLowerCaseEnum'>", str(AutoNameLowerCaseEnum))
        self.assertEqual((), AutoNameLowerCaseEnum.names())
        self.assertEqual((), AutoNameLowerCaseEnum.values())

        text = None
        print(f"{text} of_name={AutoNameLowerCaseEnum.of_name(text)}")
        self.assertEqual(None, AutoNameLowerCaseEnum.of_name(text))
        print()

    def test_ordinal_enum(self):
        print("test_ordinal_enum")
        self.assertEqual("<enum 'OrdinalEnum'>", str(OrdinalEnum))
        self.assertEqual(('EAST', 'NORTH', 'SOUTH', 'WEST'), OrdinalEnum.names())
        self.assertEqual(('EAST', 'NORTH', 'SOUTH', 'WEST'), OrdinalEnum.values())

        text = 'north'
        expected = 'OrdinalEnum <NORTH=NORTH>'
        print(f"{text} of_name={OrdinalEnum.of_name(text)}")
        self.assertEqual(expected, str(OrdinalEnum.of_name(text)))
        self.assertTrue(OrdinalEnum.equals(OrdinalEnum.NORTH, text))
        self.assertFalse(OrdinalEnum.equals(OrdinalEnum.EAST, text))

        print(f"{text} of_value={OrdinalEnum.of_value(text)}")
        self.assertEqual(None, OrdinalEnum.of_value(text))
        self.assertTrue(OrdinalEnum.equals(OrdinalEnum.NORTH, text))
        self.assertFalse(OrdinalEnum.equals(OrdinalEnum.EAST, text))

        # check isinstance of
        ordinal = OrdinalEnum.NORTH
        is_north = isinstance(ordinal, OrdinalEnum)
        print(f"{ordinal} is instance of {OrdinalEnum} = {is_north}")
        self.assertTrue(is_north)
        print()

    def test_lower_case_ordinal_enum(self):
        print("test_lower_case_ordinal_enum")
        self.assertEqual("<enum 'LowerCaseOrdinalEnum'>", str(LowerCaseOrdinalEnum))
        self.assertEqual(('EAST', 'NORTH', 'SOUTH', 'WEST'), LowerCaseOrdinalEnum.names())
        self.assertEqual(('east', 'north', 'south', 'west'), LowerCaseOrdinalEnum.values())

        text = 'north'
        expected = 'LowerCaseOrdinalEnum <NORTH=north>'
        print(f"{text} of_name={LowerCaseOrdinalEnum.of_name(text)}")
        self.assertEqual(expected, str(LowerCaseOrdinalEnum.of_name(text)))
        self.assertTrue(LowerCaseOrdinalEnum.equals(LowerCaseOrdinalEnum.NORTH, text))
        self.assertFalse(LowerCaseOrdinalEnum.equals(LowerCaseOrdinalEnum.EAST, text))

        text = 'east'
        expected = 'LowerCaseOrdinalEnum <EAST=east>'
        print(f"{text} of_value={LowerCaseOrdinalEnum.of_value(text)}")
        self.assertEqual(expected, str(LowerCaseOrdinalEnum.of_value(text)))
        self.assertTrue(LowerCaseOrdinalEnum.equals(LowerCaseOrdinalEnum.EAST, text))
        self.assertFalse(LowerCaseOrdinalEnum.equals(LowerCaseOrdinalEnum.NORTH, text))

        # check isinstance of
        ordinal = LowerCaseOrdinalEnum.NORTH
        is_north = isinstance(ordinal, LowerCaseOrdinalEnum)
        print(f"{ordinal} is instance of {LowerCaseOrdinalEnum} = {is_north}")
        self.assertTrue(is_north)
        print()

    def test_even_odd_enum(self):
        print("test_even_odd_enum")
        self.assertEqual("<enum 'EvenOddEnum'>", str(EvenOddEnum))
        self.assertEqual(('EVEN', 'ODD'), EvenOddEnum.names())
        self.assertEqual((1, 2), EvenOddEnum.values())

        text = 'even'
        expected = 'EvenOddEnum <EVEN=1>'
        print(f"{text} of_name={EvenOddEnum.of_name(text)}")
        self.assertEqual(expected, str(EvenOddEnum.of_name(text)))
        self.assertTrue(EvenOddEnum.equals(EvenOddEnum.EVEN, text))
        self.assertFalse(EvenOddEnum.equals(EvenOddEnum.ODD, text))

        text = 2
        expected = 'EvenOddEnum <ODD=2>'
        print(f"{text} of_value={EvenOddEnum.of_value(text)}")
        self.assertEqual(expected, str(EvenOddEnum.of_value(text)))
        self.assertTrue(EvenOddEnum.equals(EvenOddEnum.ODD, text))
        self.assertFalse(EvenOddEnum.equals(EvenOddEnum.EVEN, text))

        # check isinstance of
        value = EvenOddEnum.EVEN
        is_even = isinstance(value, EvenOddEnum)
        print(f"{value} is instance of {EvenOddEnum} = {is_even}")
        self.assertTrue(is_even)
        print()

    def test_log_type_enum(self):
        print("test_log_type_enum")
        self.assertEqual("<enum 'LogTypeEnum'>", str(LogTypeEnum))
        self.assertEqual(('ALL', 'DEBUG', 'INFO', 'WARN', 'ERROR'), LogTypeEnum.names())
        self.assertEqual((1, 2, 3, 4, 5), LogTypeEnum.values())

        text = 'debug'
        expected = 'LogTypeEnum <DEBUG=2>'
        print(f"{text} of_name={LogTypeEnum.of_name(text)}")
        self.assertEqual(expected, str(LogTypeEnum.of_name(text)))
        self.assertTrue(LogTypeEnum.equals(LogTypeEnum.DEBUG, text))
        self.assertFalse(LogTypeEnum.equals(LogTypeEnum.INFO, text))

        text = 3
        expected = 'LogTypeEnum <INFO=3>'
        print(f"{text} of_value={LogTypeEnum.of_value(text)}")
        self.assertEqual(expected, str(LogTypeEnum.of_value(text)))
        self.assertTrue(LogTypeEnum.equals(LogTypeEnum.INFO, text))
        self.assertFalse(LogTypeEnum.equals(LogTypeEnum.WARN, text))

        # check isinstance of
        log_type = LogTypeEnum.WARN
        is_warning = isinstance(log_type, LogTypeEnum)
        print(f"{log_type} is instance of {LogTypeEnum} = {is_warning}")
        self.assertTrue(is_warning)
        print()

    def test_http_method_enum(self):
        print("test_http_method_enum")
        self.assertEqual("<enum 'HttpMethodEnum'>", str(HttpMethodEnum))
        expected = ('CONNECT', 'HEAD', 'GET', 'POST', 'PUT', 'DELETE', 'OPTIONS', 'TRACE', 'PATCH')
        self.assertEqual(expected, HttpMethodEnum.names())
        self.assertEqual(expected, HttpMethodEnum.values())

        text = 'get'
        expected = 'HttpMethodEnum <GET=GET>'
        print(f"{text} of_name={HttpMethodEnum.of_name(text)}")
        self.assertEqual(expected, str(HttpMethodEnum.of_name(text)))
        self.assertTrue(HttpMethodEnum.equals(HttpMethodEnum.GET, text))
        self.assertFalse(HttpMethodEnum.equals(HttpMethodEnum.POST, text))

        text = 'post'
        print(f"{text} of_value={HttpMethodEnum.of_value(text)}")
        self.assertEqual(None, HttpMethodEnum.of_value(text))
        self.assertTrue(HttpMethodEnum.equals(HttpMethodEnum.POST, text))
        self.assertFalse(HttpMethodEnum.equals(HttpMethodEnum.GET, text))

        # check isinstance of
        method = HttpMethodEnum.PATCH
        is_patch = isinstance(method, HttpMethodEnum)
        print(f"{method} is instance of {HttpMethodEnum} = {is_patch}")
        self.assertTrue(is_patch)
        print()

    def test_priority_enum(self):
        logger.debug("+test_priority_enum()")
        self.assertEqual("<enum 'Priority'>", str(Priority))
        expected = ('HIGH', 'MEDIUM', 'LOW')
        self.assertEqual(expected, Priority.names())
        expected = (3, 2, 1)
        self.assertEqual(expected, Priority.values())

        text = 'MEDIUM'
        expected = 'Priority <MEDIUM=2>'
        print(f"{text} of_name={Priority.of_name(text)}")
        self.assertEqual(expected, str(Priority.of_name(text)))
        self.assertTrue(Priority.equals(Priority.MEDIUM, text))
        self.assertFalse(Priority.equals(Priority.LOW, text))

        text = 2
        print(f"{text} of_value={Priority.of_value(text)}")
        self.assertEqual(Priority.MEDIUM, Priority.of_value(text))
        self.assertTrue(Priority.equals(Priority.MEDIUM, text))
        self.assertFalse(Priority.equals(Priority.LOW, text))

        # check isinstance of
        priority = Priority.LOW
        is_priority = isinstance(priority, Priority)
        print(f"{priority} is instance of {Priority} = {is_priority}")
        self.assertTrue(is_priority)

        logger.debug("+test_priority_enum()")
        print()


# Starting point
if __name__ == 'main':
    unittest.main(exit=False)
