# Python3 code to demonstrate
# convert dictionary string to dictionary
# using ast.literal_eval()
import ast

# initializing string
test_string = '{"Nikhil" : 1, "Akshat" : 2, "Akash" : 3}'

# printing original string
print("The original string : " + str(test_string))

# using ast.literal_eval()
# convert dictionary string to dictionary
res = ast.literal_eval(test_string)

# print result
print("The converted dictionary : " + str(res))
