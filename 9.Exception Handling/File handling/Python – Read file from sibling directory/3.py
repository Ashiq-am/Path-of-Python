import os

path = os.path.realpath(__file__)
dir = os.path.dirname(path)

# replaces folder name of Sibling_1 to
# Sibling_2 in directory
dir = dir.replace('Sibling_1', 'Sibling_2')

# changes the current directory to Sibling_2
# folder
os.chdir(dir)
print(dir)
