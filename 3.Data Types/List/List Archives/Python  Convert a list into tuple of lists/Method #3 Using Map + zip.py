# Python code to convert a list into tuple of lists

# Initialisation of list
Input = ['first', 'second', 'third']

# Using Map + zip
Output = tuple(map(list, zip(Input)))

# printing output
print(Output)
