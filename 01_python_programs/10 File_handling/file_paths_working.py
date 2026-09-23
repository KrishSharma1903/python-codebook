##Creating a new directory
import os
# new_directory = "Package"
# os.mkdir(new_directory)
# print(f"Directory {new_directory} created")

##Listing files and directories
items=os.listdir('.')
print(items)

##joining Paths
dir_name="folder"
file_name="file.txt"
full_path=os.path.join(dir_name,file_name)
print(full_path)

#checking whether a file is present or not 
path = 'example1.txt'
if os.path.exists(path):
    print(f"The path {path} exists")
else:
    print(f"The path {path} does not exists")

#Checking if a path os a file or a directory
path = 'example.txt'
if os.path.isfile(path):
    print(f"The path '{path}' is a file.")
elif os.path.isdir(path):
    print(f"The path '{path}' is a directory.")
else:
    print(f"The path '{path}' is neither a file nor a directory.")

#getting the absolute path 
relative_path='example.txt'
absolute_path=os.path.abspath(relative_path)
print(absolute_path)