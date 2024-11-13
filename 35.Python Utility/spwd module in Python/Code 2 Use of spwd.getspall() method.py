# Python program to explain spwd.getspall() method

# importing spwd module
import spwd

# Get the all available
# shadow password database entries
# using spwd.getspall() method
entries = spwd.getspall()

# Print the retrieved entries
print("Shadow password database entries:")
for row in entries:
    print(row)
