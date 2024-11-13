# Python code to get positive element
# from list of list

# List Initialisation
Input = [[10, -11, 222], [42, -222, -412, 99, -87]]

# Using list comprehension
Output = [ [b for b in a if b>0] for a in Input]

# printing output
print("Initial List is :", Input)
print("Modified list is :", Output)
