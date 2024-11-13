import ast

# Converting a string representation of a list to an actual list
literal_string = "[1, 2, 3, 4]"
result = ast.literal_eval(literal_string)
print(result)
