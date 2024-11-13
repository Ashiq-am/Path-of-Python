# import os module
import os

# get source file name
src = input("Enter src filename:")

# get destination file name
destination = input("Enter target filename:")

# copies source to destination file
os.popen(f"copy {src} {destination}")
