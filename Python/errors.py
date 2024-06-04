# Author: Rohtash Lakra
import inspect

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