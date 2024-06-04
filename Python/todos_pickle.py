# Author: Rohtash Lakra
import sys
import pickle

# ToDo Class
class ToDo:

    def __init__(self, title, important = True, category = "Normal"):
        self.title = title
        self.important = important
        self.category = category

    def __repr__(self):
        return f"Todo <title={self.title}, important={self.important}, category={self.category}>"


# ToDo Manager
class ToDoManager:

    # init manager
    def __init__(self, file_name = "todos_pickle.rsl"):
        self.file_name = file_name
        self.todos = []

    # Save the object
    def save(self, todos = None):
        if todos == None:
            todos = self.todos
        # else:
        #     print("No data provided to save")

        try:
            # open file to write data in binary format
            file = open(self.file_name, "wb")
            pickle.dump(todos, file)
            file.close()
        except Exception as ex:
            print(ex)

    # Load the object
    def load(self):
        todos = []
        # open file to read binary format data
        try:
            file = open(self.file_name, "rb")
            todos = pickle.load(file)
            file.close()
        except:
            pass

        return todos

    # Add a ToDo object
    def add(self, todo):
        self.todos.append(todo)


# build objects list
# todos = [ToDo("Walk Dog"), ToDo("Eat Cheese", False), ToDo("Learn Python", category = "Work")]
# toDoManager = ToDoManager("test.rsl")
# toDoManager.save_data(todos)
# print(toDoManager.load_data())

toDoManager = ToDoManager()

# todo's list
todos = []

# Read ToDo's List
# todos.py
todos = toDoManager.load()

print(todos)

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
toDoManager.save(todos)

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
