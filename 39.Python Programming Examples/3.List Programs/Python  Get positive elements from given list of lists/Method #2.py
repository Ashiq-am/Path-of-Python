# Python code to get positive element
# from list of list

# List Initialisation
Input = [[10, -11, 222], [42, -222, -412, 99, -87]]

# Using list comprehension and map
temp = map(lambda elem: filter(lambda a: a>0, elem), Input)
Output = [[a for a in elem if a>0] for elem in temp]

# printing output
print("Initial List is :", Input)
print("Modified list is :", Output)
