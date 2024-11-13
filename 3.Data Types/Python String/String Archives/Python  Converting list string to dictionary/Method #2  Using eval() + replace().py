# Python3 code to demonstrate
# Converting list string to dictionary
# Using eval() + replace()

# initializing string
test_string = '[120:1, 190:2, 140:3]'

# printing original string
print("The original string : " + str(test_string))

# using eval() + replace()
# Converting list string to dictionary
res = eval(test_string.replace("[", "{").replace("]", "}"))

# print result
print("The dictionary after extraction is : " + str(res))
