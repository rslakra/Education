#
# Author: Rohtash Lakra
#


def divide(x, y):
    if y == 0:
        raise ArithmeticError("You can't divide by zero !")

    print(f"{x} divided by {y} is {x / y}")


print("Division")
print(divide(2, 3))
print(divide(81, 4))
print(divide(0, 2))
print()
# ZeroDivisionError: division by zero
try:
    print(divide(16, 0))
except ArithmeticError as ex:
    print(ex)

print(divide(73, 4))

# KeyError
# A KeyError occurs when trying to access a key that does not exist with dict[key].
print()
# Key Error - A KeyError occurs when trying to access a key that does not exist with dict[key]
games_dic = {'ball': 12, 'racket': 9, 'hockey': 2}
print(f"ball: {games_dic['ball']}")
key = "game"
try:
    print(f"bat: {games_dic[key]}")
except KeyError as ex:
    print(ex)

print(f"{key} in games_dic: {key in games_dic}")
# returns None if the key is not present
print(f"{key} = : {games_dic.get(key)}")
# returns 0 as default value if the key doesn't exist
print(f"{key} = : {games_dic.get(key, 0)}")
print(f"keys: {games_dic.keys()}")
print()

# NameError
# A NameError is raised when calling an attribute or function that is not defined.
title = "The python is a functional language"
print(title)
# A NameError is raised when calling an attribute or function that is not defined.
# NameError: name 'titel' is not defined.
try:
    print(f"title: {titel}")
except NameError as ex:
    print(ex)

print()

# UnicodeError
# UnicodeEncodeError and UnicodeDecodeError are raised when Python cannot encode or decode from or to Unicode.
partyGame = "Piñata"
print(f"partyGame: {partyGame}")
# UnicodeEncodeError: 'ascii' codec can't encode character '\xf1' in position 2: ordinal not in range(128)
encodedPartyGameAscii = None
try:
    encodedPartyGameAscii = partyGame.encode('ascii')
except UnicodeError as ex:
    print(ex)
print(f"encodedPartyGameAscii: {encodedPartyGameAscii}")
encodedPartyGameUtf8 = partyGame.encode('utf8')
print(f"encodedPartyGameUtf8: {encodedPartyGameUtf8}")
decodedPartyGameUtf8 = encodedPartyGameUtf8.decode('utf8')
print(f"decodedPartyGameUtf8: {decodedPartyGameUtf8}")
assert partyGame == decodedPartyGameUtf8
print()
# The values are strict, replace, ignore, and backslashreplace.
# While strict will return a UnicodeDecodeError the other arguments allow you to handle the encoded character without
# raising an error:
print(f"decoded using ascii : {encodedPartyGameUtf8.decode('ascii', 'replace')}")
print(f"decoded using ascii : {encodedPartyGameUtf8.decode('ascii', 'ignore')}")
print(f"decoded using ascii : {encodedPartyGameUtf8.decode('ascii', 'backslashreplace')}")
print()

# TypeError
# A TypeError occurs when an object is the wrong type for the action you are attempting to execute.
num = 2
try:
    # TypeError: can only concatenate str (not "int") to str
    print("3" + 2)
except Exception as ex:
    print(f"{type(ex)} - {ex}")

print()

# AttributeError
# The AttributeError is raised when you try to access an attribute on an object that doesn’t have that attribute defined.
nums = (range(5))
print(nums)
print()

try:
    # AttributeError: 'range' object has no attribute 'append'
    nums.append(16)
except Exception as ex:
    print(f"{type(ex)} - {ex}")
print()

print(f"{nums[0]} - {nums[-1]}")
# IndexError The IndexError is raised when you attempt to retrieve an index from a sequence, like a list or a tuple,
# and the index isn’t found in the sequence.
try:
    # AttributeError: 'range' object has no attribute 'append'
    nums.__getitem__(16)
except Exception as ex:
    print(f"{type(ex)} - {ex}")
print()


# SyntaxError
# The SyntaxError is raised when you have incorrect Python syntax in your code.

# Define a 'greet()' function
def greet(name):
    print(f"Hello, {name}")


print()
print(greet("Roh"))
print()

print("-" * 80)

print("Before")


# Custom Exception
class EmptyTextError(Exception):

    def __init__(self, *args: object):
        super().__init__(*args)


def upper_case(text):
    if len(text) == 0:
        raise EmptyTextError("The 'text' should be provided!")

    return text.upper()


try:

    upper_case("Rohtash")
    upper_case("")
    result = 4 / 0
    print(f"Result:{result}")

except NameError as ex:
    print(f"{ex}!")
except ZeroDivisionError as ex:
    print(f"{ex}!")
except EmptyTextError as ex:
    print(f"{ex}!")
except Exception as ex:
    print(f"{ex}!")

print("After")
