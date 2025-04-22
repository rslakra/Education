# Author: Rohtash Lakra
import os



def print_dir(folders):
    print(f"\nAll Files:")
    for folder in folders:
        print(folder)

dirs = os.listdir()
print(dirs)

# Print All files
print_dir(dirs)
# for dir in dirs:
#     print(dir)


# read items of a specific folder
dir_name = "../.."
data = os.listdir(dir_name)
print_dir(data)
print("\n")