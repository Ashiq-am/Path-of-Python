# Python program to explain grp.getgrnam() method

# importing grp module
import grp

# Group name
name = "ihritik"

# Get the group
# database entry for the
# specified group name
# using grp.getgrnam() method
entry = grp.getgrnam(name)

# Print the retrieved entry
print("Group database entry for the group name '%s':" % name)
print(entry)

# Group name
name = "root"

# Get the group
# database entry for the
# specified group name
# using grp.getgrnam() method
entry = grp.getgrnam(name)

# Print the retrieved entry
print("\nGroup database entry for the group name '% s':" % name)
print(entry)
