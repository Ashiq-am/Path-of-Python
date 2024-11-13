# Python3 code to demonstrate working of
# Consecutive Pair Maximum
# Using loop + max()

# initializing list
test_list = [5, 8, 3, 5, 9, 10]

# printing list
print("The original list : " + str(test_list))

# Consecutive Pair Maximum
# Using loop + max()
res = []
for ele in range(0, len(test_list), 2):
	res.append(max(test_list[ele], test_list[ele + 1]))

# Printing result
print("Pair maximum of list : " + str(res))
