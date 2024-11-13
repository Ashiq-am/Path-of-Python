# Python program to explain os.path.relpath() method

# importing os module
import os

# Path
path = "/home / User / Desktop / file.txt"

# Path of Start directory
start = "/home / User"

# Compute the relative file path
# to the given path from the
# the given start directory.
relative_path = os.path.relpath(path, start)

# Print the relative file path
# to the given path from the
# the given start directory.
print(relative_path)

# Path
path = "/home / User / Desktop / file.txt"

# Compute the relative file path
# to the given path from the
# the current directory.

# if we do not specify the start
# parameter it will default to
# os.curdir i.e current directory
relative_path = os.path.relpath(path)

# Print the relative file path
# to the given path from the
# the given start directory.
print(relative_path)

# Path
path = "/home / User / Desktop / file.txt"

# Path of Start directory
start = "GeeksForGeeks / home"

# Compute the relative file path
# to the given path from the
# the given start directory.
relative_path = os.path.relpath(path, start)

# Print the relative file path
# to the given path from the
# the given start directory.
print(relative_path)

# Path
path = "/home / User / Desktop / file.txt"

# Path of Start directory
start = "/home / User / ihritik / file.txt"

# Compute the relative file path
# to the given path from the
# the given start directory.
relative_path = os.path.relpath(path, start)

# Print the relative file path
# to the given path from the
# the given start directory.
print(relative_path)
