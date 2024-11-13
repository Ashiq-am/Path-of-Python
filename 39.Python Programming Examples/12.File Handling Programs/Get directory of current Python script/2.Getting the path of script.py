# Python program to get the
# path of the script


import os

# Get the current working
# directory (CWD)
cwd = os.getcwd()
print("Current Directory:", cwd)

# Get the directory of
# script
script = os.path.realpath(__file__)
print("SCript path:", script)
