# Python program to explain os.remove() method

# importing os module
import os

# File name
file = 'file.txt'

# File location
location = "/home/User/Documents"

# Path
path = os.path.join(location, file)

# Remove the file
# 'file.txt'
os.remove(path)
print("%s has been removed successfully" % file)
