#
# Author: Rohtash Lakra
#
import inspect


def full_name(first_name: str, last_name: str, middle_name: str = None) -> str:
    """Returns the full-name based on the provided parameters"""
    if first_name and middle_name and last_name:
        return "{} {} {}".format(first_name.title(), middle_name.title(), last_name.title())
    elif first_name and last_name:
        return "{} {}".format(first_name.title(), last_name.title())
    # elif first_name and middle_name:
    #     return "{} {}".format(first_name.title(), middle_name.title())
    # elif middle_name and last_name:
    #     return "{} {}".format(middle_name.title(), middle_name.title())
    elif first_name:
        return first_name.title()
    elif last_name:
        return last_name.title()

    return None


def to_title_case(items: list[str]) -> list[str]:
    """As the list is a type that contains some internal types, you put them in square brackets"""
    title_case_list = []
    for item in items:
        title_case_list.append(item.title())
        # print(item)

    return title_case_list


def process_dictionary(prices: dict[str, float] = {}) -> dict[float, list[str]]:
    items: dict[float, list[str]] = {}
    # print(f"prices={prices}")
    if prices:
        for key, value in prices.items():
            # print(f"key={key}, value={value}, type={type(value)}, items={items}")
            # if list(items.keys()).count(value) == 1:
            if value in items.keys():
                items[value].append(key)
            else:
                items[value] = [key]

    return items


def getClassName(self) -> str:
    """Returns the name of the class."""
    return type(self).__name__


def getMethodName(self) -> str:
    """Returns the name of the class."""
    # return type(self).__qualname__
    return inspect.stack()[0][3]
