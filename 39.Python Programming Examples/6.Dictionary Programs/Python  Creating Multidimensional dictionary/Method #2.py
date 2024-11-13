# Python3 code to demonstrate working of
# Creating Multidimensional dictionary
# Using defaultdict()
from collections import defaultdict

# Utiliy function to create dictionary
def multi_dict(K, type):
	if K == 1:
		return defaultdict(type)
	else:
		return defaultdict(lambda: multi_dict(K-1, type))

# Initialize dictionary
test_dict = {}

# printing original dictionary
print("The original dictionary : " + str(test_dict))

# Using defaultdict()
# Creating Multidimensional dictionary
# calling function
test_dict = multi_dict(3, int)
test_dict[2][3][4] = 1

# printing result
print("Dictionary after nesting : " + str(dict(test_dict)))
