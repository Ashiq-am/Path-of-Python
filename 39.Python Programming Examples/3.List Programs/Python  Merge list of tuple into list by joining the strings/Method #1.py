# Python code to convert list of tuple into list
# by joining elements of tuple

# Input list initialisation
Input = [('Hello', 'There'), ('Namastey', 'India'), ('Incredible', 'India')]

# using join and list comprehension
Output = ['_'.join(temp) for temp in Input]

# printing output
print(Output)
