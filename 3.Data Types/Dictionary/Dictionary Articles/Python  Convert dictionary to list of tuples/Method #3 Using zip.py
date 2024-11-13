# Python code to convert dictionary into list of tuples

# Initialization of dictionary
dict = { 'Geeks': 10, 'for': 12, 'Geek': 31 }

# Using zip
listt = zip(dict.keys(), dict.values())

# Converting from zip object to list object
listt = list(listt)

# Printing list
print(listt)
