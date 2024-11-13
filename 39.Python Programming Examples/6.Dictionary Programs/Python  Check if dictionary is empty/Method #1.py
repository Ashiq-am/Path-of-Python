# Python3 code to demonstrate
# Check if dictionary is empty
# using bool()

# initializing empty dictionary
test_dict = {}

# printing original dictionary
print("The original dictionary : " + str(test_dict))

# using bool()
# Check if dictionary is empty
res = not bool(test_dict)

# print result
print("Is dictionary empty ? : " + str(res))
