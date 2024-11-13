# import os library
import os

# get source file name
src = input("Enter src filename:")

# get destination file name
dest = input("Enter dest filename:")

# rename source file name with destination file name
os.rename(src, dest)
