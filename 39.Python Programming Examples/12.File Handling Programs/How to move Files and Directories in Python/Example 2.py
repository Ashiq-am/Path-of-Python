# Python program to move
# files and directories


import shutil

# Source path
source = "D:\Pycharm projects\gfg\Test\A"

# Destination path
destination = "D:\Pycharm projects\gfg\Test\G"

# Move the content of
# source to destination
dest = shutil.move(source, destination, copy_function = shutil.copytree)

# print(dest) prints the
# Destination of moved directory
