# Python program to explain os.mkdir() method

# importing os module
import os

# path
path = 'D:/Pycharm projects / GeeksForGeeks'

# Create the directory
# 'GeeksForGeeks' in
# '/home / User / Documents'
try:
    os.mkdir(path)
except OSError as error:
    print(error)
