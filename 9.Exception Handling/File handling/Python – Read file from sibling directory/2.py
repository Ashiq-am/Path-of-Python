import os

# gives the path of demo.py
path = os.path.realpath(__file__)

# gives the directory where demo.py
# exists
dir = os.path.dirname(path)
print(dir)
