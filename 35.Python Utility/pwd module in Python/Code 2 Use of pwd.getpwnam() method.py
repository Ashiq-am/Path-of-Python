# Python program to explain pwd.getpwnam() method

# importing pwd module
import pwd

# User name
name = "ihritik"

# Get the password
# database entry for the
# specified username
# using pwd.getpwnam() method
entry = pwd.getpwnam(name)

# Print the retrieved entry
print("Password database entry for '% s':" % name)
print(entry)

# User name
name = "root"

# Get the password
# database entry for the
# specified username
# using pwd.getpwnam() method
entry = pwd.getpwnam(name)

# Print the retrieved entry
print("\nPassword database entry for '% s':" % name)
print(entry)
