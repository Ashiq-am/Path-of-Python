# Python program to explain grp.getgrall() method

# importing grp module
import grp

# Get the all available group
# database entries
# using grp.getgrall() method
entries = grp.getgrall()

# Print the retrieved entry
print("Group database entries:")

for row in entries:
    print(row)
