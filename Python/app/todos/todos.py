# Author: Rohtash Lakra
import sys

file_name = "todos.txt"

# todo's list
todos = []

# Read ToDo's List
# todos.py
try:
    file = open(file_name, "r")
    todos = file.readlines()
    file.close()
except:
    pass

# print(todos)

# To Add ToDo Items
# todos.py add "Lean Python"
# do operations on the file
if len(sys.argv) >= 3 and sys.argv[1].lower() == "add":
    # make sure the cursor is at the next line
    if len(todos) > 0 and not todos[len(todos) - 1].endswith("\n"):
        todos[len(todos) - 1] += "\n"
    todos.append(f"{sys.argv[2]}\n")
    # print(todos)

# To Remove/Complete Task
# todos.py remove 2
if len(sys.argv) >= 3 and sys.argv[1].lower() == "remove":
    try:
        deleteIndex = int(sys.argv[2])
        if deleteIndex > 0 and deleteIndex <= len(todos):
            del(todos[deleteIndex - 1])
        else:
            print(f"\nInvalid Index:{deleteIndex}\n")
    except Exception as ex:
        print(f"Invalid Input: {sys.argv[2]}\n")
        sys.exit(1)

    # print(todos)

# Save ToDo's Items
try:
    file = open(file_name, "w")
    # todos = list(map(lambda item: item + "\n", todos))
    file.writelines(todos)
    file.close()
except:
    pass

# Print ToDo's Items
print(f"\nCurrent ToDo's:")
if len(todos) > 0:
    for index in range(len(todos)):
        # print(f"{index + 1}. {todos[index].rstrip()}")
        print(f"{index + 1}. {todos[index]}", end="")
else:
    print(f"Great! All work is done. :)")

# Usage Syntax
print(f"\n****************")
print(f"\nTo View ToDo's:\n{sys.argv[0]}")
print(f"\nTo Add Item in ToDo's:\n{sys.argv[0]} add \"Lean Python\"")
print(f"\nTo Remove/Complete Item in ToDo's:\n{sys.argv[0]} remove 2\n")
