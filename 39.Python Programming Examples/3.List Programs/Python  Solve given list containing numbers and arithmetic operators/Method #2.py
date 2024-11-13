# Python code to solve the list
# containing numbers and arithmetic operators

# Input list initialization
lst = [2, '+', 22, '+', 55, '+', 4]

# Using eval and join
Output = eval(' '.join(str(x) for x in lst))

# Printing output
print("Initial list", lst)
print("Answer after solving list is:", Output)
