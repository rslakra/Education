# Author: Rohtash Lakra

import sys

total = 1
# print all arguments of the command
del(sys.argv[0]) # remove first argument - filename
for arg in sys.argv:
    try:
        # num = int(arg)
        num = float(arg)
        total *= num
    except Exception as ex:
        print(f"\nOnly numbers are allowed!")
        print(f"{ex}\n")
        sys.exit(1) # quit executing further

print(f"\nResult: {total}\n")

