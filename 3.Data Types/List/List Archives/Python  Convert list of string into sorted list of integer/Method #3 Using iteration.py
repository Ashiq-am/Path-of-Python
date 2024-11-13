# Python code to convert list of
# string into sorted list of integer

# List initialization
list_string = ['11', '1', '58', '15', '0']

# using iteration and sorted()
list_sorted = sorted(int(x) for x in list_string)

# printing output
print(list_sorted)
