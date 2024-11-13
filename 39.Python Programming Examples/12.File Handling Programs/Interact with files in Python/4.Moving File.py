# Python program to move
# files


import shutil

# Source path
source = "D:\Pycharm projects\gfg\Test\Test4.txt"

# Destination path
destination = "D:\Pycharm projects\gfg\Test\G"

# Move the content of
# source to destination
dest = shutil.move(source, destination)

# print(dest) prints the
# Destination of moved directory
