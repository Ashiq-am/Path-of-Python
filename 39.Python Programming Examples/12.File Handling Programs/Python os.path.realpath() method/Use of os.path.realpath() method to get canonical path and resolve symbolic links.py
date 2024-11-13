# Python program to explain os.path.realpath() method

# importing os module
import os

# Path
path = "/home / ihritik / Desktop / file(shortcut).txt"

# Get the canonical path
# of the specified path
# by eliminating any symbolic links
# encountered in the path
real_path = os.path.realpath(path)

# Print the canonical path
print(real_path)

# Path
path = "/../../GeeksForGeeks / sample.py"

# Get the canonical path
# of the specified path
# eliminating any symbolic links
# encountered in the path
real_path = os.path.realpath(path)

# Print the canonical path
print(real_path)

# Path
path = "file.txt"

# Get the canonical path
# of the specified path
# eliminating any symbolic links
# encountered in the path
real_path = os.path.realpath(path)

# Print the canonical path
print(real_path)

os.chdir("/home / ihritik / Downloads/")

# Path
path = "file.txt"

# Get the canonical path
# of the specified path
# eliminating any symbolic links
# encountered in the path
real_path = os.path.realpath(path)

# Print the canonical path
print(real_path)
