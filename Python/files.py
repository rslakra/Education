# Author: Rohtash Lakra
import sys

print(f"\nApi Version: {sys.api_version}, \nPlatform:{sys.platform}\n")


# read/write files

# file = open("test.txt", "x") # x means to create a new file
# file.write("File opened in write mode and writing this text.")
# file.close() # close the file to avoid resource leak

# file = open("test.txt", "w") # w means to override a file and if not exists, create a new file
# file.write("File opened in override mode.")
# file.close() # close the file to avoid resource leak

# file = open("test.txt", "a") # a means to append to a file. If it doen't exist, create a new file
# file.write("File opened to append more data to file.")
# file.close() # close the file to avoid resource leak


# # create a file, which name passed as argument and write the rest args into file.
# if len(sys.argv) <= 1:
#     print("Filename must provide!")
#     sys.exit(1)

# # read filename
# file_name = sys.argv[1]
# file = open(file_name, "a")
# del(sys.argv[0])
# del(sys.argv[0])

# # read all args and write to file
# for arg in sys.argv:
#     file.write(arg)
#     file.write(" ")

# # close the file
# file.close()


# # open a file to read from it
# file = open("files.py", "r") # r stands for read-only
# # text = file.read()
# # print(text)

# # Before reading all lines, make sure to reopen the file,
# # because if you already read, there is nothing to read
# # read all lines of the file
# lines = file.readlines()
# # print(lines)
# for line in lines:
#     print(line)

# file.close() # close the file


file = open("numbers.txt", "r")
lines = file.readlines()
file.close()
# print(lines)
# total = 1;
# for line in lines:
#     num = float(line)
#     total *= num

# remove '\n' from the line
numbers = list(map(lambda line: float(line.rstrip()), lines))
print(f"\nFile Numbers: {numbers}")


print("\nReduce")
from functools import reduce
result = reduce(lambda total, num: total * num, numbers)
print(result)
