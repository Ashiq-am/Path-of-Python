# Python3 code to demonstrate working of
# Add K to Minimum element in Column Tuple List
# Using min() + loop

# initializing lists
test_list = [(4, 5), (3, 2), (2, 2), (4, 6), (3, 2), (4, 5)]

# printing original list
print("The original list is : " + str(test_list))

# initializing K
K = 5

# Add K to Minimum element in Column Tuple List
# Using min() + loop
a_min = min(a for a, b in test_list)
b_min = min(b for a, b in test_list)
res = []

for a, b in test_list:
	if a == a_min and b == b_min:
		res.append((a + K, b + K))
	elif a == a_min :
		res.append((a + K, b))
	elif b == b_min:
		res.append((a, b + K))
	else :
		res.append((a, b))

# printing result
print("Tuple after modification : " + str(res))
