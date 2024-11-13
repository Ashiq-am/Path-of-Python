# Python3 code to demonstrate working of
# Join Tuples to Integers in Tuple List
# Using loop

# helpr_fnc
def join_tup(tup):
	res = tup[0]
	for idx in tup[1:]:
		res = res * 10 + idx
	return res

# initializing list
test_list = [(4, 5), (5, 6), (1, 3), (6, 9)]

# printing original list
print("The original list is : " + str(test_list))

# Join Tuples to Integers in Tuple List
# Using loop
res = [join_tup(idx) for idx in test_list]

# printing result
print("The joined result : " + str(res))
