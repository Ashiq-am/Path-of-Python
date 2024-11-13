# Python code to convert a list into tuple of lists

# Initialisation of list
Input = ['first', 'second', 'third']

# Using map + lambda
Output = tuple(map(lambda x: [x], Input))

# printing output
print(Output)
