# Python program to explain shutil.chown() method

# importing shutil module
import shutil

# importing Path class of pathlib module
from pathlib import Path

# Path
path = '/home/ihritik/Desktop/file.txt'

# Get the owner and group
# of the specified path
# using Path.owner() and
# Path.group() method
info = Path(path)
user = info.owner()
group = info.group()

# Print owner and group
# of the specified path
print("Current owner and group of the specified path")
print("Owner:", user)
print("Group:", group)

# Now, change the owner and group
# of the specified path
user = 'ihritik'
group = 'ihritik'
shutil.chown(path, user, group)

print("\nOwner and group changed")

# Print the owner and group
# of the specified path
info = Path(path)
user = info.owner()
group = info.group()
print("Current owner:", user)
print("Current group:", group)

# Change only group
# of the specified path
# and let owner as it is
group = 'root'

shutil.chown(path, group=group)

print("\nOnly group changed")

# Print the owner and
# group of the speicifed path
info = Path(path)
user = info.owner()
group = info.group()
print("Current owner:", user)
print("Current group:", group)

# Similarly, we can change
# only owner of the
# specified path and let
# group as it is
