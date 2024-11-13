# Python program to explain os.makedirs() method

# importing os module
import os

# os.makedirs() method will raise
# an OSError if the directory
# to be created already exists


# Directory
directory = "Nikhil"

# Parent Directory path
parent_dir = "D:/Pycharm projects/GeeksForGeeks/Authors"

# Path
path = os.path.join(parent_dir, directory)

# Create the directory
# 'Nikhil'
os.makedirs(path)
print("Directory '% s' created" % directory)
