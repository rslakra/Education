#
# Author: Rohtash Lakra
#
import json

food_json = {
    "id": "0001",
    "type": "donut",
    "name": "Cake",
    "ppu": 0.55
}

print()
print("Food's JSON")
print(food_json)
print()

food_dict = {}
for key in food_json:
    food_dict[key] = food_json[key]

print()
print("Food's Dictionary")
print(food_dict)
print()

# food_obj = json.loads(food)
# food_obj = json.loads(food_json, object_hook=lambda entry: namedtuple('Food', entry.keys())(*entry.values()))

# check not empty
if food_dict:
    for key in food_dict:
        print(f"{key} = {food_dict.get(key)}")

#  check emtpy
if not food_dict:
    print("food_dict is emtpy")

data = [{"name": "tobi", "class": "1", "age": "14", "gender": "m"},
        {"name": "joke", "class": "1", "age": "18", "gender": "f"},
        {"name": "mary", "class": "2", "age": "14", "gender": "f"},
        {"name": "kano", "class": "2", "age": "15", "gender": "m"},
        {"name": "ada", "class": "1", "age": "15", "gender": "f"},
        {"name": "bola", "class": "2", "age": "10", "gender": "f"},
        {"name": "fake", "class": "1", "age": "15", "gender": "m"}]

print()


def process_request(request_json):
    if len(request_json) == 0:
        return None

    if not request_json.get('metadata'):
        request_json['metadata'] = {}

    metadata = request_json.get('metadata')
    if not metadata.get('message'):
        metadata['message'] = {
            "event": "canceled",
            "action": "end_call",
            "audience": "expert"
        }

    # add event in the metadata
    request_json['metadata'] = json.dumps(metadata)

    return request_json


print()
print(json.dumps(process_request({"status": "canceled"})))
print()
request_json = {
    "status": "canceled",
    "metadata": {"make": "Honda", "year": "2024", "model": "Civic"}
}
print(json.dumps(process_request(request_json)))
print()


body = {
    "idProperty": "email",
    "inputs": [
        {
            "id": "email@email.com"
        }
    ]
}

print()
print(f"body={json.dumps(body)}")
print(f"body['inputs'][0] = {body['inputs'][0]}")
print(f"id = {body['inputs'][0].get('id')}")
print()