# Python program to explain shutil.chown() method

# We can also change owner
# and group of the specified path
# by passing owner id (uid) and
# group id (gid) as parameter
# instead of passing name of
# owner and / or group


# importing shutil module
import shutil

# importing Path class of pathlib module
from pathlib import Path

# Path
path = '/home/ihritik/Desktop/file.txt'

# Get the owner user and
# group of the speicifed path
# using Path.owner() and
# Path.group() method
info = Path(path)
user = info.owner()
group = info.group()
print("Current owner and group of the specified path")
print("Current owner:", user)
print("Current group:", group)

# Now, change the owner user
# and group of the
# specified path

uid = 0
gid = 0
shutil.chown(path, uid, gid)

print("\nOwner and group changed")

# Print the owner user and
# group of the speicifed path
info = Path(path)
user = info.owner()
group = info.group()
print("Current owner:", user)
print("Current group:", group)
