# importing os module
import os

# gives the path of demo.py
path = os.path.realpath(__file__)

# gives the directory where demo.py
# exists
dir = os.path.dirname(path)

# replaces folder name of Sibling_1 to
# Sibling_2 in directory
dir = dir.replace('Sibling_1', 'Sibling_2')

# changes the current directory to
# Sibling_2 folder
os.chdir(dir)

# opening file.txt which is to read
f = open('file.txt')

# reading data from file.txt and storing
# it in data
data = f.read()

# printing data
print(data)
