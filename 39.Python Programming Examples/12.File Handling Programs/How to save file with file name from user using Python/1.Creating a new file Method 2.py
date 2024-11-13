# import pathlib module
import pathlib

# path of this script
directory = "D:\gfg\\"

# get fileName from user
filepath = directory + input("Enter filename:")

# To create a file
pathlib.Path(filepath).touch()
