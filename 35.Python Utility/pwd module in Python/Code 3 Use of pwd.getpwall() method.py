# Python program to explain pwd.getpwall() method

# importing pwd module
import pwd

# Get the list
# of all available password
# database entries using
# pwd.getpwall() method
entries = pwd.getpwall()

# Print the list
print("Password database entries:")
for row in entries:
    print(row)
