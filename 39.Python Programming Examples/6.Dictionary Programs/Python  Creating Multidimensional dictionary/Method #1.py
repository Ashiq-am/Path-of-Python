# Python3 code to demonstrate working of
# Creating Multidimensional dictionary
# Using setdefault()

# Initialize dictionary
test_dict = {}

# printing original dictionary
print("The original dictionary : " + str(test_dict))

# Using setdefault()
# Creating Multidimensional dictionary
test_dict.setdefault(1, {})[4] = 7

# printing result
print("Dictionary after nesting : " + str(test_dict))
