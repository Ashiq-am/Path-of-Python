# Python code to check whether
# suffix exists in list of strings.

# Input list initialization
lst = ["Paras", "Geeksforgeeks", "Game"]

# using any to find suffix
Output = any('Geek' in x for x in lst)

# Printing output
print("Initial List is :", lst)
print(Output)
