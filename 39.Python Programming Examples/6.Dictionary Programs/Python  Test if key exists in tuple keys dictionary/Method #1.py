# Python3 code to demonstrate working of
# Test if key exists in tuple keys dictionary
# using any() + generator expression

# initialize dictionary
test_dict = {(4, 5) : '1', (8, 9) : '2', (10, 11) : '3'}

# printing original dictionary
print("The original dictionary : " + str(test_dict))

# Test key
key = 10

# Test if key exists in tuple keys dictionary
# using any() + generator expression
res = any(key in sub for sub in test_dict)

# printing result
print("Does key exists in dictionary? : " + str(res))
