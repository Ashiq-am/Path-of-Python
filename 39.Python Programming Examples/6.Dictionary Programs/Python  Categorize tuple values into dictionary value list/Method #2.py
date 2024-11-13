# Python3 code to demonstrate working of
# Categorize tuple values into dictionary value list
# Using dict() + list comprehension + frozenset()

# Initialize list of tuples
test_list = [(1, 3), (1, 4), (2, 3), (3, 2), (5, 3), (6, 4)]

# printing original list
print("The original list : " + str(test_list))

# Using dict() + list comprehension + frozenset()
# Categorize tuple values into dictionary value list
res = dict((key, [i[0] for i in test_list if i[1] == key])
			for key in frozenset(j[1] for j in test_list))

# printing result
print("The dictionary converted from tuple list : " + str(res))
