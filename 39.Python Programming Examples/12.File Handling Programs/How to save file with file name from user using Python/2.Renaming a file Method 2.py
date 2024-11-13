# import pathlib module
import pathlib

# get source file name
src = input("Enter src filename:")

# get destination file name
target = input("Enter target filename:")

# rename source file name with target file name
pathlib.Path(src).rename(target)
