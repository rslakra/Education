# Author: Rohtash Lakra
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
    def __init__(self, file_name = "todos.rsl"):
        self.file_name = file_name


    # Save the object
    def save_data(self, todos):
        # open file to write data in binary format
        file = open(self.file_name, "wb")
        pickle.dump(todos, file)
        file.close()

    # Load the object
    def load_data(self):
        # open file to read binary format data
        file = open(self.file_name, "rb")
        todos = pickle.load(file)
        file.close()
        return todos


# build objects list
todos = [ToDo("Walk Dog"), ToDo("Eat Cheese", False), ToDo("Learn Python", category = "Work")]
print(todos)

toDoManager = ToDoManager()
# save
toDoManager.save_data(todos)
# load
data = toDoManager.load_data()
print(f"\ntodos:{todos}\n data:{data}")


# # pickle fun
# items = [12, 35, 3, 45]
# # write binary data
# file = open("pickle.rsl", "wb")
# pickle.dump(items, file)
# file.close()
# # read binary data
# file = open("pickle.rsl", "rb")
# items_loaded = pickle.load(file)
# file.close()

# print(f"age:{items}, age_loaded:{items_loaded}")
