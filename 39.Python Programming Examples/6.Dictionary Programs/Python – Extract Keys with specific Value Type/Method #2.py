# Python3 code to demonstrate working of
# Extract Keys with specific Value Type
# Using list comprehension + isinstance()

# initializing dictionary
test_dict = {'gfg': 2, 'is': 'hello', 'best': 2, 'for': {'1': 3}, 'geeks': 4}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

# initializing type
targ_type = int

# one-liner to solve the problem
res = [key for key, val in test_dict.items() if isinstance(val, targ_type)]

# printing result
print("The extracted keys : " + str(res))
