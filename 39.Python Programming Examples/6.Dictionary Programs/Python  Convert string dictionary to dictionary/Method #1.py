# Python3 code to demonstrate
# convert dictionary string to dictionary
# using json.loads()
import json

# initializing string
test_string = '{"Nikhil" : 1, "Akshat" : 2, "Akash" : 3}'

# printing original string
print("The original string : " + str(test_string))

# using json.loads()
# convert dictionary string to dictionary
res = json.loads(test_string)

# print result
print("The converted dictionary : " + str(res))
