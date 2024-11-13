# Python code to convert dictionary into list of tuples

# Initialization of dictionary
dict = { 'Geeks': 10, 'for': 12, 'Geek': 31 }

# Converting into list of tuple
list = [(k, v) for k, v in dict.items()]

# Printing list of tuple
print(list)
