# Python implementation of converting
# a string into a dictionary

# importing ast module
import ast

# initialising string dictionary
str = '{"Jan" : "January", "Feb" : "February", "Mar" : "March"}'

# converting string into dictionary
dictionary = ast.literal_eval(str)

# printing the generated dictionary
print(dictionary)
