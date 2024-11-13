# Python code for printing to stderr

# importing the package
# for sys.stderr
import sys

# variables
Company = "Geeksofrgeeks.org"
Location = "Noida"
Email = "contact@geeksforgeeks.org"

# print to stderr
print(Company, Location, Email, file=sys.stderr)
