# Python program to explain grp.getgrgid() method

# importing grp module
import grp

# Group id
gid = 1000

# Get the group
# database entry for the
# specified group id
# using grp.getgrgid() method
entry = grp.getgrgid(gid)

# Print the retrieved entry
print("Group database entry for group id % s:" % gid)
print(entry)

# Group id
gid = 0

# Get the group
# database entry for the
# specified group id
# using grp.getgrgid() method
entry = grp.getgrgid(gid)

# Print the retrieved entry
print("\nGroup database entry for group id % s:" % gid)
print(entry)
