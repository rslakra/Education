# Python Enums
# Author: Rohtash Lakra
# Reference - https://docs.python.org/3/howto/enum.html
#
import sys
from datetime import date
from enum import Enum, auto, unique, IntEnum, IntFlag
from typing import Any


# @unique
class BaseEnum(Enum):
    """
    Base Enum for all other Enums. For readability, add constants in Alphabetical order.
    Also, subclassing an enumeration is allowed only if the enumeration does not define any members.
    """

    def __str__(self):
        return f"{self.__class__.__name__} <{self.name}{'=' + str(self.value) if self.value else ''}>"

    def __repr__(self):
        return self.__str__()

    @classmethod
    def names(cls):
        "Returns the list of enum name"
        names = []
        for member in cls:
            if member and member.name:
                names.append(member.name)

        return tuple(names)

    @classmethod
    def of_name(cls, name: str) -> Enum:
        "Returns the Service Request Type object based on request_type param"
        if name is not None:
            for member in cls:
                if member.name.lower() == name.lower():
                    return member

        return None

    @classmethod
    def values(cls):
        "Returns the list of enum values"
        values = []
        for member in cls:
            if member and member.value:
                values.append(member.value)

        return tuple(values)

    @classmethod
    def of_value(cls, value: Any) -> Enum:
        "Returns the Service Request Type object based on request_type param"
        if value is not None:
            for member in cls:
                if member.value == value:
                    return member

        return None

    @classmethod
    def equals(cls, enum_type: Enum, text: Any) -> bool:
        "Returns true if the text is either equals to name or value of an enum otherwise false"
        if enum_type is None:
            raise ValueError('enum_type should provide!')
        if text is None:
            raise ValueError('text should provide!')

        return enum_type == cls.of_name(str(text)) or enum_type == cls.of_value(text)


class AutoNameEnum(BaseEnum):
    """
    AutoName automatically names enum members. For readability, add constants in Alphabetical order.
    Also, subclassing an enumeration is allowed only if the enumeration does not define any members.
    """

    @staticmethod
    def _generate_next_value_(name, start, count, last_values):
        return name


# Auto lowercase name
class AutoNameLowerCaseEnum(BaseEnum):
    """
    AutoNameLowerCaseEnum automatically lowercase names of enum members. For readability, add constants in Alphabetical order.
    Also, subclassing an enumeration is allowed only if the enumeration does not define any members.
    """

    @staticmethod
    def _generate_next_value_(name, start, count, last_values):
        return name.lower()


# Define Colors Enum
class ColorEnum(BaseEnum):
    """Color Enum represents the various colors. For readability, add constants in Alphabetical order."""
    RED = 1
    GREEN = 2
    BLUE = 3
    RGB = 3


# Define Weekday Enum
class WeekDaysEnum(BaseEnum):
    """WeekDay Enum represents the days of the week. For readability, add constants in Alphabetical order."""
    SUNDAY = 1
    MONDAY = 2
    TUESDAY = 3
    WEDNESDAY = 4
    THURSDAY = 5
    FRIDAY = 6
    SATURDAY = 7
    WEEKEND = SATURDAY | SUNDAY

    # add a method to return the weekday from the date
    # @param date
    @classmethod
    def from_date(cls, date):
        return cls(date.isoweekday())

    # add a method to return the today's weekday.
    @classmethod
    def today(cls):
        return cls.from_date(date.today())


# In cases where the actual values of the members do not matter,
# you can save yourself some work and use auto() for the values:
class NumberEnum(BaseEnum):
    """Number types Enum. For readability, add constants in Alphabetical order."""
    EVEN = auto()
    ODD = auto()
    PRIME = auto()


class ShapeEnum(BaseEnum):
    """Shape Enum defines various shapes. For readability, add constants in Alphabetical order."""
    CIRCLE = 1
    DIAMOND = 2
    SQUARE = 3
    DIAMOND_ALIAS = 2

    @classmethod
    def all_shapes(cls):
        """
        Note that the aliases Shape.DIAMOND_ALIAS and WeekDay.WEEKEND aren’t shown.
        The special 'attribute __members__' is a read-only ordered mapping of names to members.
        It includes all names defined in the enumeration, including the aliases:
        all_shapes = list([name, entry for name, entry in Shape.__members__().items()])

        # The special attribute __members__ is a read-only ordered mapping of names to members.

        :return:
        """
        # return cls(list(Shape.__members__.items()))
        # returns (name, Enum) as list
        return list(cls.__members__.items())


# Ensuring unique enumeration values
@unique
class UniqueShapeEnum(BaseEnum):
    """Unique Shape Enum defines various shapes. For readability, add constants in Alphabetical order."""
    CIRCLE = 1
    DIAMOND = 2
    SQUARE = 3


# Using automatic values
class StatusEnum(BaseEnum):
    """Status Enum defines various statuses. For readability, add constants in Alphabetical order."""

    # The values are chosen by _generate_next_value_() static, which can be overridden:
    # Note The _generate_next_value_() method must be defined before any members.
    @staticmethod
    def _generate_next_value_(name, start, count, last_values):
        return name.lower()

    ENABLED = auto()
    DISABLED = auto()
    MODIFIED = auto()
    DELETED = auto()

    """
    _missing_(cls, value)
    A 'classmethod' for looking up values not found in cls. 
    By default it does nothing, but can be overridden to implement custom search behavior:
    """

    @classmethod
    def _missing_(cls, value):
        value = value.lower()
        for member in cls:
            if member.value == value:
                return member

        return None


# Ordinal Enum
class OrdinalEnum(AutoNameEnum):
    """OrdinalEnum defines all 4 ordinals. For readability, add constants in Alphabetical order."""

    EAST = auto()
    NORTH = auto()
    SOUTH = auto()
    WEST = auto()


# LowerCase Ordinal Enum
class LowerCaseOrdinalEnum(AutoNameLowerCaseEnum):
    """LowerCaseOrdinalEnum defines all 4 ordinals in lowercase. For readability, add constants in Alphabetical order."""

    EAST = auto()
    NORTH = auto()
    SOUTH = auto()
    WEST = auto()


class EvenOddEnum(BaseEnum, IntFlag):
    """EvenOddEnum defines even and odd enums. For readability, add constants in Alphabetical order."""

    EVEN = auto()
    ODD = auto()


class LogTypeEnum(BaseEnum, IntEnum):
    """LogTypeEnum defines various log levels. For readability, add constants in Alphabetical order."""
    ALL = auto()
    DEBUG = auto()
    INFO = auto()
    WARN = auto()
    ERROR = auto()


print()
print(f"Sys Version: {sys.version_info}")
print()
# String Enum
if sys.version_info >= (3, 11):
    from enum import StrEnum


    # from strenum import StrEnum
    class HttpMethodEnum(StrEnum):
        """HttpMethod enums defines supported http methods. For readability, add constants in Alphabetical order."""

        GET = auto()
        HEAD = auto()
        POST = auto()
        PUT = auto()
        DELETE = auto()
        CONNECT = auto()
        OPTIONS = auto()
        TRACE = auto()
        PATCH = auto()
else:
    @unique
    class HttpMethodEnum(AutoNameEnum):
        """HttpMethod enums defines supported http methods. For readability, add constants in Alphabetical order."""
        CONNECT = auto()
        HEAD = auto()
        GET = auto()
        POST = auto()
        PUT = auto()
        DELETE = auto()
        OPTIONS = auto()
        TRACE = auto()
        PATCH = auto()

        """
        _missing_(cls, value)
        A 'classmethod' for looking up values not found in cls. 
        By default it does nothing, but can be overridden to implement custom search behavior:
        """

        @classmethod
        def _missing_(cls, value):
            value = value.upper()
            for member in cls:
                if member.value == value:
                    return member

            return None


class HookType(BaseEnum):
    """HookType Enum"""
    BEFORE_ALL = 'before_all'  # Runs once before all tests.
    AFTER_ALL = 'after_all'  # Runs once after all tests.
    BEFORE_FEATURE = 'before_feature'  # Runs before each feature file is tested.
    AFTER_FEATURE = 'after_feature'  # Runs after each feature file has been tested.
    BEFORE_SCENARIO = 'before_scenario'  # Runs before each scenario.
    AFTER_SCENARIO = 'after_scenario'  # Runs after each scenario.
    BEFORE_STEP = 'before_step'  # Runs before each step.
    AFTER_STEP = 'after_step'  # Runs before each step.
    BEFORE_TAG = 'before_tag'  # Runs before each tag.
    AFTER_TAG = 'after_tag'  # Runs before each tag.


print()
print(HookType)
print(HookType.names())
print()
for hook_type in HookType.names():
    print(f"hook_type={hook_type}, type={type(hook_type)}")
print()


class MessagePriority(BaseEnum):
    CRITICAL = 3
    IMPORTANT = 2
    NEUTRAL = 1


class Priority(BaseEnum, IntEnum):
    HIGH = 3
    MEDIUM = 2
    LOW = 1
