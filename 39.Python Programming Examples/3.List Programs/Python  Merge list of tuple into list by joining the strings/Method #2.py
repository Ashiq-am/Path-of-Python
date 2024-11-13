# Python code to convert list of tuple into list
# by joining elements of tuple

# Input list initialisation
Input = [('Hello', 'There'), ('Namastey', 'India'), ('Incredible', 'India')]

# using map and join
Output = list(map('_'.join, Input))

# printing output
print(Output)
