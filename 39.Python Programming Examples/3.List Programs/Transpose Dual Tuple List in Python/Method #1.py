# Python3 code to demonstrate working of
# Transpose Tuple List
# Using loop

# hlper_fnc function
def hlper_fnc(test_list):
	# declare empty list
	sub1 = []
	sub2 = []

	res = (sub1, sub2)
	for sub in test_list:
		# add element in the last of the list
		sub1.append(sub[0])
		sub2.append(sub[1])

	return res

# initializing list
test_list = [(5, 1), (3, 4), (9, 7), (10, 6)]

# printing original list
print("The original list is : " + str(test_list))

# Transpose Tuple List
# Using loop
res = hlper_fnc(test_list)

# printing result
print("The transposed tuple list : " + str(res))
