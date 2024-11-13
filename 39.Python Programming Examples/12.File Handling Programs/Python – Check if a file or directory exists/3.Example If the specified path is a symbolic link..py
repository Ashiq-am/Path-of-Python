# Python program to explain os.path.isdir() method

# importing os.path module
import os.path

# Create a directory
# (in current working directory)
dirname = "GeeksForGeeks"
os.mkdir(dirname)

# Create a symbolic link
# pointing to above directory
symlink_path = "/home/User/Desktop/gfg"
os.symlink(dirname, symlink_path)

path = dirname

# Now, Check whether the
# specified path is an
# existing directory or not
isdir = os.path.isdir(path)
print(isdir)

path = symlink_path

# Check whether the
# specified path (which is a
# symbolic link ) is an
# existing directory or not
isdir = os.path.isdir(path)
print(isdir)
