"""
Author: Rohtash Lakra

Implements Utils.
"""
__author__ = 'Rohtash Lakra (work.lakra@gmail.com)'

import hashlib
import json
import uuid
from enum import Enum
from pathlib import Path
from typing import Callable, TypeVar, List, Dict, Iterator

from core.enums import HttpMethodEnum

# These type variables are used by the container types.
_T = TypeVar('T')  # Key type
_E = TypeVar('E')  # Value type
_K = TypeVar('K')  # Key type
_V = TypeVar('V')  # Value type


class Utils(Enum):
    """
    Prints Arguments

    @:param args - tuple of positional arguments

    *args - collects additional positional arguments into a tuple, not a list. The arguments are accessible using tuple indexing and iteration.
    """

    @staticmethod
    def print_args(*args):
        for arg in args:
            print(arg)
        # for count, arg in enumerate(args):
        # print('{0}. {1}'.format(count, arg))

    """
    Prints Keyword Arguments
    
    @:param kwargs - dictionary of keyword arguments (keyword arguments (**kwargs) to a function)
    """

    @staticmethod
    def print_kwargs(**kwargs):
        # print(f"kwargs={kwargs}")
        for key, value in kwargs.items():
            print("%s = %s" % (key, value))
            # print('{0} = {1}'.format(key, value))

    """
    Generates Unique UUID
    """

    @classmethod
    def generate_uuid(cls):
        return uuid.uuid4().hex

    """
    Parses User-Agent
    """

    @classmethod
    def parse_user_agent(cls, user_agent_str):
        translator = str.maketrans('', '', '{}\"')
        user_agent = user_agent_str.translate(translator)
        # print(f"user-agent:{user_agent}")

        # break the user-agent into tokens and build dictionary of key/value pair and return it.
        return {
            key.strip(): value.strip() if not value.isnumeric() else int(value.strip())
            for key, value in (token.split(':') for token in user_agent.split(',') if len(token.split(':')) == 2)
        }

    """
    Executes an HTTP Request
    """

    @staticmethod
    def execute(url, method=None):
        import urllib.request
        import ssl
        ssl.get_default_verify_paths()

        # validate the url is provided
        if len(url) == 0:
            raise ValueError("The <url> must provide!")

        # check the method provided
        if method is None:
            method = HttpMethodEnum.GET

        result = None
        try:
            req = urllib.request.Request(url, method)
            with urllib.request.urlopen(req, context=ssl.create_default_context()) as response:
                result = response.read()
        except Exception as ex:
            print(ex)
            raise ex

        return result

    @staticmethod
    def group_by(items: Iterator[_V],
                 *,
                 key: Callable[[_V], _K],
                 ) -> Dict[_K, List[_V]]:
        """Groups items based on whether they produce the same key from a function.

        Args:
            items: The items to group.
            key: Items that produce the same value from this function get grouped together.

        Returns:
            A dictionary mapping outputs that were produced by the grouping function to
            the list of items that produced that output.

        Examples:
            >>> group_by([1, 2, 3], key=lambda i: i == 2)
            {False: [1, 3], True: [2]}

            >>> group_by(range(10), key=lambda i: i % 3)
            {0: [0, 3, 6, 9], 1: [1, 4, 7], 2: [2, 5, 8]}

            >>> Utils.group_by(json_data, key=lambda k: k['class'])
            {"mammal": [{"name": "leopard", "class": "mammal", "order": "Carnivora", "max_speed": "58.0"}], "bird": [{"name": "parrot", "class": "bird", "order": "Psittaciformes", "max_speed": "24.0"}]}
        """

        results: Dict[_K, List[_V]] = {}

        for item in items:
            # results.setdefault(value, set()).add(key)
            group_key = key(item)
            # print(f"group_key => {group_key}, item => {item}")
            results.setdefault(group_key, list()).append(item)

        return results

    @staticmethod
    def isValidString(text) -> bool:
        """Return true if there's only a valid char and excludes whitespace characters and false otherwise."""
        return True if text and (not text.isspace()) else False

    @staticmethod
    def toStr(class_: _T) -> str:
        strBuilder = class_.__name__ + " <"
        claStr = ''
        try:
            claStr += "{}".format(
                {
                    key: value for key, value in class_.__dict__.items() if not str(hex(id(value))) in str(value)
                }
            )
        except:
            print(f"Error processing '{class_}' class!")

        print(f"claStr: {claStr}")

        attrs = [getattr(class_, p) for p in dir(class_) if not p.startswith('_')]
        print(f"attrs: {attrs}")

        # atts =  [(x, eval('type(x.%s).__name__' % x)) for x in dir(class_)]
        # print(f"atts: {atts}")

        # cls_attrs = dir(type(class_))
        # attrs = {}
        # for attr_name in cls_attrs:
        #     if hasattr(class_, attr_name):
        #         try:
        #             attr_value = getattr(class_, attr_name)
        #             print(f"\n{attr_name}: {attr_value}")
        #             attrs[attr_name] = attr_value
        #         except AttributeError:
        #             print(f"Unable to retrieve '{attr_name}' of class: {class_}")

        strBuilder += ">"
        print(f"strBuilder: {strBuilder}")
        return strBuilder


class IOUtils(Enum):

    @classmethod
    def read_json_file(cls, file_path):
        filePath = Path(file_path);
        if not filePath.exists():
            raise Exception(f"'{file_path}' doesn't exist!")
        elif filePath.is_dir():
            raise Exception(f"'{file_path}' is not a file!")

        contents = None
        # read the file contents
        with open(filePath, 'r') as file:
            contents = file.read()

        # print(f"{type(json.loads(contents))}")

        return json.loads(contents) if contents else None


user_agent = '{platform: "iOS", osVersion: "1.0", deviceType: "mobile/tablet", deviceId: "1234-5678-9014", appVersion: "1.0.0"}'
print(f"user_agent:{user_agent}")
print("Parsed User-Agent:")
print(Utils.parse_user_agent(user_agent))
print()

print()
print("Execute HTTP Request")
url = 'https://www.python.org/'
# print(Utils.execute(url))
print()

print()
print(f"Reads File")
json_data = IOUtils.read_json_file("data/animals.json")
print(json_data)

# print()
# print("---------------<Group by Class>---------------")
# group_by_class = {}
# for entry in json_data:
#     print(entry)
#     print(entry.pop(['class']))
#     # group_by_class.setdefault(entry.pop(['class']), []).append(entry)
#
# print(json.dumps(group_by_class))
# print("---------------<Group by Class>---------------")
print()

print()
print("Group by Class type")
group_by_class = {}
group_by_class = Utils.group_by(json_data, key=lambda k: k['class'])
print(json.dumps(group_by_class))
print()


class Pair:

    def __init__(self, key, value):
        self.key = key
        self.value = value

    # def update(self, pair_dic):
    #     for key, value in pair_dic.items():
    #         setattr(self, key, value)

    # def __str__(self):
    #     return f"Pair <key={self.key}, value={self.value}>"
    #
    # def __repr__(self):
    #     return self.__str__()


print()
print("Pair class as string")
pair_str = Utils.toStr(Pair)
print(pair_str)
print()


class SecurityUtils(Enum):

    @staticmethod
    def sha256_hash(text: str):
        sha256_hash = hashlib.sha256(text.encode())
        base64_hash = sha256_hash.digest().hex()
        return base64_hash

    @staticmethod
    def sha256_hash_with_salt(hashed_text: str, salt: str):
        salt_bytes = bytes(salt, 'utf-8')
        salt_sha256_hash = hashlib.sha256(salt_bytes)
        salt_digest = salt_sha256_hash.digest()

        salt_base64 = salt_bytes.hex()
        hash_base64 = hashed_text + salt_digest.hex()

        return salt_base64, hash_base64

    @staticmethod
    def sha256_hash_with_random_salt(hashed_text: str):
        return SecurityUtils.sha256_hash_with_salt(hashed_text, Utils.generate_uuid())

    @staticmethod
    def verify_hash(text, salt, hash):
        salt_bytes = bytes.fromhex(salt)
        hash_bytes = bytes.fromhex(hash)

        salt_digest = hashlib.sha256(salt_bytes).digest()
        text_digest = hashlib.sha256(text.encode()).digest()

        return (text_digest + salt_digest) == hash_bytes


print()
print("SecurityUtils")
print("sha256_hash")
plain_text = 'Rohtash'
base64_hash = SecurityUtils.sha256_hash(plain_text)
print(f"plain_text:{plain_text}, base64_hash:{base64_hash}")
base64_hash_expected = '5c9c41e81eaa1174a8b33c78cf192d1c3a7762438e40f89275b96852a1dea3e9'
assert base64_hash_expected == base64_hash
print()
print("sha256_hash")
plain_text = 'Rohtash'
default_salt = Utils.generate_uuid()
sha256_hash = SecurityUtils.sha256_hash(plain_text)
print(f"plain_text:{plain_text}, default_salt:{default_salt}, sha256_hash:{sha256_hash}")
salt, hashed_text = SecurityUtils.sha256_hash_with_salt(sha256_hash, default_salt)
print(f"salt:{salt}, hashed_text:{hashed_text}")
is_verified = SecurityUtils.verify_hash(plain_text, salt, hashed_text)
print(f"is_verified:{is_verified}")
print()


class JsonUtils(Enum):

    def ensure_valid_dictionary(json_text):
        """Ensure action_data is a dictionary"""
        print(f'json_text={json_text}')
        json_data = {}
        if isinstance(json_text, str):
            try:
                json_data = json.loads(json_text)
            except json.JSONDecodeError:
                print('Invalid json_text={}'.format(json_text))
                json_data = {}

        return json_data
