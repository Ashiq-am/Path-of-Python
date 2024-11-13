# Python program to explain shutil.copytree() method


# importing shutil module
import shutil

# path
path = 'D:/Pycharm projects/GeeksforGeeks/'

# Source path
src = 'D:/Pycharm projects/GeeksforGeeks/src'

# Destination path
dest = 'D:/Pycharm projects/GeeksforGeeks/dst'

# Copy the content of
# source to destination
destination = shutil.copytree(src, dest)

# print(destination) prints the
# path of newly created file
