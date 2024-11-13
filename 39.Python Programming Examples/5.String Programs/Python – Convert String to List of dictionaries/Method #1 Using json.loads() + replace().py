# Python3 code to demonstrate working of
# Convert String to List of dictionaries
# Using json.loads + replace()
import json

# initializing string
test_str = ["[{'Gfg' : 3, 'Best' : 8}, {'Gfg' : 4, 'Best' : 9}]"]

# printing original string
print("The original string is : " + str(test_str))

# replace() used to replace strings
# loads() used to convert
res = [json.loads(idx.replace("'", '"')) for idx in test_str]

# printing result
print("Converted list of dictionaries : " + str(res))
