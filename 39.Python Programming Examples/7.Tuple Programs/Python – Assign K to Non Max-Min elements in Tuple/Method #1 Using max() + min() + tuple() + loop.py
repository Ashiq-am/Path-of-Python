# Python3 code to demonstrate working of
# Assign K to Non Max-Min elements in Tuple
# Using min() + max() + loop + tuple()

# initializing tuple
test_tuple = (5, 6, 3, 6, 10, 34)

# printing original tuple
print("The original tuple : " + str(test_tuple))

# initializing K
K = 4

# Assign K to Non Max-Min elements in Tuple
# Using min() + max() + loop + tuple()
res = []
for ele in test_tuple:
	if ele not in [max(test_tuple), min(test_tuple)]:
		res.append(K)
	else:
		res.append(ele)
res = tuple(res)

# printing result
print("The tuple after conversion: " + str(res))
