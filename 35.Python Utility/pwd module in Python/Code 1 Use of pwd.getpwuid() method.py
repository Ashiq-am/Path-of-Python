# Python program to explain pwd.getpwuid() method

# importing pwd module
import pwd

# User id
uid = 1000

# Get the password
# database entry for the
# specified user id
# using pwd.getpwuid() method
entry = pwd.getpwuid(uid)

# Print the retrieved entry
print("Password database entry for user id : % d:" % uid)
print(entry)

# User id
uid = 0

# Get the password
# database entry for the
# specified user id
# using pwd.getpwuid() method
entry = pwd.getpwuid(uid)

# Print the retrieved entry
print("Password database entry for user id : % d:" % uid)
print(entry)
