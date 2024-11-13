# Python program to list out
# all the sub-directories and files


import os

# List comprehension to enter
# all directories to list

L = [(root, dirs, files) for root, dirs, files, in os.walk('Test')]

print("List of all sub-directories and files:")
for i in L:
    print(i)
