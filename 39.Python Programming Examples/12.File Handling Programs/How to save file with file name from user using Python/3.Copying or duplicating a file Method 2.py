# import shutil module
import shutil

# get source file name
src = input("Enter src filename:")

# get destination file name
dest = input("Enter target filename:")

# copies source file to a new destination file
shutil.copyfile(src, dest)
