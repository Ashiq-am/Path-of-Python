# Python code to convert dictionary into list of tuples

# Initialization of dictionary
dict = { 'Geeks': 10, 'for': 12, 'Geek': 31 }

# Initialization of empty list
list = []

# Iteration
for i in dict:
    k = (i, dict[i])
    list.append(k)

# Printing list
print(list)
