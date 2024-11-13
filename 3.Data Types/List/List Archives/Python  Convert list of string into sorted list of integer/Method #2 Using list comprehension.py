# Python code to convert list of
# string into sorted list of integer

# List initialization
list_string = ['11', '1', '58', '15', '0']

# Using list comprehension
output = [int(x) for x in list_string]

# using sort function
output.sort()

# Printing output
print(output)
