#
# Author: Rohtash Lakra
#
from pathlib import Path
import datetime

print()
base_dir = Path.cwd()
print(f"base_dir: {base_dir}")

def print_folder(base_dir: Path):
    print()
    print(f"----------------<{base_dir.name}>----------------")
    print(f"Parent: {base_dir.parent}")
    print(f"Is Folder: {base_dir.is_dir()}")
    print(f"Is Symlink: {base_dir.is_symlink()}")
    print(f"Is File: {base_dir.is_file()}")
    print(f"Exists: {base_dir.exists()}")
    print(f"Name: {base_dir.name}")
    print(f"CWD: {base_dir.cwd()}")
    print(f"Home: {base_dir.home()}")
    print(f"Owner: {base_dir.owner()}")
    print(f"Absolute: {base_dir.absolute()}")
    print(f"Parts: {base_dir.parts}")

# print folder
print_folder(base_dir)

print()
for entry in base_dir.iterdir():
    print_folder(entry)

print()
date = datetime.date.today()
today_logs = Path.cwd().joinpath("logs",str(date), "*.txt")
print(f"today_logs={today_logs}")

def print_attributes(file_path):
    print()
    print("--------------------------------------------")
    filePath = Path(file_path)
    print(f"Find me here <{filePath.parent}>")
    print(f"filePath: {filePath}")
    print(f"exists: {filePath.exists()}")
    print(f"is_file: {filePath.is_file()}")
    print(f"is_dir: {filePath.is_dir()}")
    print(f"is_symlink: {filePath.is_symlink()}")
    print(f"is_mount: {filePath.is_mount()}")
    print(f"is_char_device: {filePath.is_char_device()}")
    print(f"is_absolute: {filePath.is_absolute()}")
    print(f"only name: {filePath.stem}")
    print(f"file extension: {filePath.suffix}")
    print(f"path separator: {filePath.anchor}")
    print("--------------------------------------------")
    print()

print()
print(f"Find me here <{Path(__file__).parent}>")
log_file_path = Path(__file__).parent.parent.joinpath("sql", "logs.sql")
print(f"log_file_path: {log_file_path}>")
print_attributes(log_file_path)

data_dir = Path.cwd() / "data"
print_attributes(data_dir)
print(f"data_dir: {data_dir}")
print()
# date = datetime.date.today()
# today_logs = Path.cwd().joinpath("logs",str(date), "*.txt")
# print(f"today_logs={today_logs}")


# Read Shopping list
shopping_list_filename = "shopping_list.md"
shopping_list_path = Path().joinpath(data_dir, shopping_list_filename)
print_attributes(shopping_list_path)
# Reading the file contents
with shopping_list_path.open(mode="r", encoding="utf-8") as md_file:
    contents = md_file.read()
    groceries = [line for line in contents.splitlines() if line.startswith("*")]
print("\n".join(groceries))
print()

# without opening the file, directly read the contents of it.
contents_text = shopping_list_path.read_text(encoding="utf-8")
groceries = [line for line in contents.splitlines() if line.startswith("*")]
print("\n".join(groceries))
print()

grocery_file_path = Path(__file__).parent.joinpath("groceries.md")
groceries_md = grocery_file_path.write_text("\n".join(groceries), encoding="utf-8")
print(f"grocery_file_path:{grocery_file_path} = groceries_md:{groceries_md}")
print()


#counting Path objects
from collections import Counter
basic_dir = Path(__file__).parent
print(f"basic_dir:{basic_dir}")
object_count = Counter(path.suffix for path in basic_dir.iterdir())
print(object_count)
print()


# Prints the tree of folder
def print_files_tree(folder):
    print(f"+ {folder}")
    for path in sorted(folder.rglob("*")):
        depth = len(path.relative_to(folder).parts)
        spaces = "    " * depth
        print(f"{spaces}+ {path.name}")

# print tree of this project
print(f"basic_dir:{basic_dir}")
print_files_tree(basic_dir)
print()

# import datetime
# time, file_path = max((path.stat().st_mtime, path) for path in basic_dir.iterdir())
# print(datetime.fromtimestampe(time), file_path)
# print()

# Create a unique file under the folder
def create_unique_file(folder, name_pattern):
    counter = 0
    while True:
        counter += 1
        path = folder / name_pattern.format(counter)
        if not path.exists():
            return path


#
temp_folder = Path.cwd() / "temp"
template = "rsl{:03d}.txt"
unique_file_name = create_unique_file(temp_folder, template)
# if not unique_file_name.exists():
#     unique_file_name.touch()
# unique_file_name.write_text("temp_folder")
print(f"unique_file_name: {unique_file_name}")
print()
