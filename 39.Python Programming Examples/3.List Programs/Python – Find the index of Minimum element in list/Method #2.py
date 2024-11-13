# Python3 code to demonstrate working of
# Minimum element indices in list
# Using loop + min()

# initializing list
test_list = [2, 5, 6, 2, 3, 2]

# printing list
print("The original list : " + str(test_list))

# Minimum element indices in list
# Using loop + min()
temp = min(test_list)
res = []
for idx in range(0, len(test_list)):
	if temp == test_list[idx]:
		res.append(idx)

# Printing result
print("The Positions of minimum element : " + str(res))
