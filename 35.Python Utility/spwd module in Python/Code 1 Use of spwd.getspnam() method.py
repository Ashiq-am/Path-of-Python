# Python program to explain spwd.getspnam() method

# importing spwd module
import spwd

# User name
name = "ihritik"

# Get the shadow password
# database entry for the
# specified user name
# using spwd.getspnam() method
entry = spwd.getspnam(name)

# Print the retrieved entry
print("Shadow password database entry for the user name '%s':" % name)
print(entry)

# User name
name = "root"

# Get the shadow password
# database entry for the
# specified user name
# using spwd.getspnam() method
entry = spwd.getspnam(name)

# Print the retrieved entry
print("\nShadow password database entry for the user name '%s':" % name)
print(entry)
