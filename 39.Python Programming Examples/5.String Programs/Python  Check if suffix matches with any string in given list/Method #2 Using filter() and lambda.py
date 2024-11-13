# Python code to check whether
# suffix exists in list of strings.

# Input list initialization
lst = ["Paras", "Geeksforgeeks", "Game"]

# Using filter and lambda
Output = len(list(filter(lambda x: "Jai" in x, lst))) != 0

# Printing output
print("Initial List is :", lst)
print(Output)
