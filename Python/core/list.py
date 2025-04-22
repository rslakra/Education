# mutable adts
import json

scientist_json = [
    {
        "name": "Rohtash",
        "field": "Computer Science",
        "born_year": 1975,
        "win_prize": "false"
    },
    {
        "name": "Lakra",
        "field": "English",
        "born_year": 1978,
        "win_prize": "false"
    }
]

# mutable adts objects
print()
print(scientist_json)

print()
print(scientist_json[1]["name"])
print()

print()
scientist_json[1]["name"] = 'Rohtash Singh'
print(scientist_json[1]["name"])
print()

# immutable collections
import collections

Scientist = collections.namedtuple("Scientist", [
    "name",
    "field",
    "born_year",
    "win_prize"
])

from pprint import pprint

print("----------------->")

# add scientists in the immutable list
scientists = []
for scientist in scientist_json:
    print(scientist)
    scientists.append(Scientist(scientist["name"], scientist["field"], scientist["born_year"], scientist["win_prize"]))

scientists_tuple = (scientists)

print("<--------- scientists -------->")
pprint(scientists)

# read first scientist
rohtash = scientists[1]
print("<--------- rohtash -------->")
print(rohtash)
print()

print("<--------- read named-tuple key -------->")
print()
# rohtash.name = "Rohtash Lakra"
print(rohtash.name)
# print(rohtash)
print()

print("<--------- scientists_response -------->")
scientists_response = []
for scientist in scientist_json:
    scientists_response.append(
        Scientist(scientist["name"], scientist["field"], scientist["born_year"], scientist["win_prize"]))

print(scientists_response)
print()
for response in scientists_response:
    # print(response)
    print(f"scientist <{response.name}, {response.field}, {response.born_year}, {response.win_prize}>")

print()

print("<--------- scientists_result -------->")
scientists_result = [Scientist._make({
    'name': scientist["name"],
    'field': scientist["field"],
    'born_year': scientist["born_year"],
    'win_prize': 'Yes' if scientist["win_prize"] == 'true' else "No"
}) for scientist in scientist_json]

print(scientists_result)
print()

print("<--------- results_by_expend -------->")
results_by_expend = []
results_by_expend.extend([{
    'name': scientist["name"],
    'field': scientist["field"],
    'born_year': scientist["born_year"],
    'win_prize': 'Yes' if scientist["win_prize"] == 'true' else "No"
} for scientist in scientist_json])
results_by_expend.extend([{
    'name': scientist["name"],
    'field': scientist["field"],
    'born_year': scientist["born_year"],
    'win_prize': 'Yes' if scientist["win_prize"] == 'true' else "No"
} for scientist in scientist_json])
print(results_by_expend)
print()

print("---------> scientists_tuple <--------")
print(scientists_tuple)
del scientists_tuple[0]
print()
print(scientists_tuple[0].name)

# Foods Handling
foods_json = [
    {
        "id": "0001",
        "type": "donut",
        "name": "Cake",
        "ppu": 0.55,
        "batters":
            {
                "batter":
                    [
                        {"id": "1001", "type": "Regular"},
                        {"id": "1002", "type": "Chocolate"},
                        {"id": "1003", "type": "Blueberry"},
                        {"id": "1004", "type": "Devil's Food"}
                    ]
            },
        "topping":
            [
                {"id": "5001", "type": "None"},
                {"id": "5002", "type": "Glazed"},
                {"id": "5005", "type": "Sugar"},
                {"id": "5007", "type": "Powdered Sugar"},
                {"id": "5006", "type": "Chocolate with Sprinkles"},
                {"id": "5003", "type": "Chocolate"},
                {"id": "5004", "type": "Maple"}
            ]
    },
    {
        "id": "0002",
        "type": "donut",
        "name": "Raised",
        "ppu": 0.55,
        "batters":
            {
                "batter":
                    [
                        {"id": "1001", "type": "Regular"}
                    ]
            },
        "topping":
            [
                {"id": "5001", "type": "None"},
                {"id": "5002", "type": "Glazed"},
                {"id": "5005", "type": "Sugar"},
                {"id": "5003", "type": "Chocolate"},
                {"id": "5004", "type": "Maple"}
            ]
    },
    {
        "id": "0003",
        "type": "donut",
        "name": "Old Fashioned",
        "ppu": 0.55,
        "batters":
            {
                "batter":
                    [
                        {"id": "1001", "type": "Regular"},
                        {"id": "1002", "type": "Chocolate"}
                    ]
            },
        "topping":
            [
                {"id": "5001", "type": "None"},
                {"id": "5002", "type": "Glazed"},
                {"id": "5003", "type": "Chocolate"},
                {"id": "5004", "type": "Maple"}
            ]
    }
]


# Prints Foods Dictionary
def print_dictionary(items):
    """
    Prints the dictionary items

    :param items:
    """
    print("----------------> Dictionary - items < --------------")
    print(items)
    print()


print_dictionary(foods_json)



# def printFoods(food):
#     print("----------------> food object < --------------")
#     print(food)
#     print()
#     print(f'Food <id={foods["id"]}, type={foods["type"]}, name={foods["name"]}, ppu={foods["ppu"]}>')
#     print()
#
#
# printFoods(foods=foods_json)


#
# List of foods
#
from enums import Enum

class FoodField(Enum):
    ID = "id"
    TYPE = "type"
    NAME = "name"
    PPU = "ppu"


print()
print("----------------> food object < --------------")
print(f"FoodField={FoodField}")
print(FoodField.ID)
print(f"FoodField <FoodField.ID={FoodField.ID}, name={FoodField.ID.name}, value={FoodField.ID.value}>")
print()


# Build named tuple
Food = collections.namedtuple("Food", ["id", "type", "name", "ppu"])

def convert_dictiony_to_named_tuple(food):
    return Food(id=food["id"], type=food["type"], name=food["name"], ppu=food["ppu"])


foods = []
for food in foods_json:
    foods.append(convert_dictiony_to_named_tuple(food))
    # foods.append(Food(id=food["id"], type=food["type"], name=food["name"], ppu=food["ppu"]))

print("----------------> foods < --------------")
print(foods)
print()

print()
print("----------------> action_json < --------------")
action = """
    {
        "type": "connect",
        "data": {
            "id": "3f726b39489c4c73847475c247f74c11",
            "last_call_time": "2024-07-18 19:54:14"
        }
    }
"""


action_json = json.loads(action)
print(action_json)
print(f"type: {action_json.get('type')}")
print(f"data -> id: {action_json.get('data').get('id')}")
id = action_json.get('data').get('id')
ids = [action_json.get('data').get('id')]
print(f"ids: {ids}")
# iterable may be either a sequence, a container that supports iteration, or an iterator object.
# If iterable is already a list, a copy is made and returned
id_list = list(id)
print(f"id_list: {id_list}")
print(f"list(ids): {list(ids)}")
# print(f"list().append: {list().append(id)}")
list_ids = list()
list_ids.append(id)
print(f"list_ids: {list_ids}")
ids_list = list([id])
print(f"ids_list: {ids_list}")
print()

# range, list and set
ids = list(range(1, 21))
print(f"ids={ids}")
exclude = list(range(1, 10, 3))
print(f"exclude={exclude}")
invalid = [11, 15, 21, 23]
print(f"invalid={invalid}")
unique_ids = list(set(ids) - set(exclude + invalid))
print(f"unique_ids={unique_ids}")
difference = list(set(ids).difference(set(exclude + invalid)))
print(f"difference={difference}")
brackets_list = range(5)
print(f"brackets_list={brackets_list}")

invalid_ids = []
if invalid_ids:
    print(f"invalid_ids={invalid_ids}")
else:
    print("No IDs found!")

print()
if not invalid_ids:
    print("invalid_ids is empty")
else:
    print(f"invalid_ids={invalid_ids}")
print()