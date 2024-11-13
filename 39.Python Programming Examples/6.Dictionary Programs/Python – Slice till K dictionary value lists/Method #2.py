# Python3 code to demonstrate working of
# Slice till K dictionary value lists
# Using dictionary comprehension + list slicing

# initializing dictionary
test_dict = {"Gfg" : [1, 6, 3, 5, 7],
			"Best" : [5, 4, 2, 8, 9],
			"is" : [4, 6, 8, 4, 2]}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

# initializing K
K = 4

# one-liner to slice elements of list
# items() used to get all key-value pair of dictionary
res = {key: val[:K] for key, val in test_dict.items()}

# printing result
print("The dictionary after conversion " + str(res))
