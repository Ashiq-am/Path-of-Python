# Python3 code to demonstrate working of
# Categorize tuple values into dictionary value list
# Using setdefault() + loop

# Initialize list of tuples
test_list = [(1, 3), (1, 4), (2, 3), (3, 2), (5, 3), (6, 4)]

# printing original list
print("The original list : " + str(test_list))

# Using setdefault() + loop
# Categorize tuple values into dictionary value list
res = {}
for i, j in test_list:
	res.setdefault(j, []).append(i)

# printing result
print("The dictionary converted from tuple list : " + str(res))
