# Python code to demonstrate working of
# Filter dictionary of tuples by condition
# Using lambda + filter()

# initializing dictionary
test_dict = {'a' : (6, 3), 'b' : (4, 8), 'c' : (8, 4)}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

# Filter dictionary of tuples by condition
# Using lambda + filter()
res = dict(filter(lambda x, y, z: y >= 6 and z <= 4, test_dict.items()))

# printing result
print("The filtered dictionary is : " + str(res))
