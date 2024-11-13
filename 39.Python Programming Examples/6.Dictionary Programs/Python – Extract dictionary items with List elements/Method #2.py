# Python3 code to demonstrate working of
# Extract dictionary items with List elements
# Using all() + dictionary comprehension

# initializing dictionary
test_dict = {'gfg': [4, 6], 'is': [10], 'best': [4, 5, 7]}

# printing original dictionary
print("The original dictionary : " + str(test_dict))

# initializing req_list
req_list = [4, 6, 10]

# Extract dictionary items with List elements
# Using all() + dictionary comprehension
res = {key: val for key, val in test_dict.items() if all(vals in req_list for vals in val)}

# printing result
print("The extracted dictionary: " + str(res))
