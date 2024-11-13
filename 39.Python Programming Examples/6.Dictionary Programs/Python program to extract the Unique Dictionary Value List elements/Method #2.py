# Python3 code to demonstrate working of
# Unique Dictionary Value List elements
# Using set() + union()

# initializing dictionary
test_dict = {"Gfg" : [6, 7, 4, 6],
			"is" : [8, 9, 5],
			"for" : [2, 5, 3, 7],
			"Geeks" : [6, 8, 5, 2]}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

# using * operator to get union
res = list(set().union(*test_dict.values()))

# printing result
print("Extracted items : " + str(res))
