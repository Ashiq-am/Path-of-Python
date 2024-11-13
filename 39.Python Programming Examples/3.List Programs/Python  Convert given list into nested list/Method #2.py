# Python code to convert list
# of string into list of list

# importing
import ast

# List Initialization
Input = ['12, 454', '15.72, 82.85', '52.236, 25256', '95.9492, 72.906']

# using ast to convert
Output = [list(ast.literal_eval(x)) for x in Input]

# printing
print(Output)
