# Python3 code to demonstrate working of
# Dual Tuple Alternate summation
# Using loop

# initializing list
test_list = [(4, 1), (5, 6), (3, 5), (7, 5), (1, 10)]

# printing original list
print("The original list is : " + str(test_list))

res = 0
for idx in range(len(test_list)):

	# checking for Alternate element
	if idx % 2 == 0:
		res += test_list[idx][0]
	else:
		res += test_list[idx][1]

# printing result
print("Summation of Alternate elements of tuples : " + str(res))
