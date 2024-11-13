# Python3 code to demonstrate working of
# Count Bidirectional Tuple Pairs
# Using loop

# initializing list
test_list = [(5, 6), (1, 2), (6, 5), (9, 1), (6, 5), (2, 1)]

# printing original list
print("The original list is : " + str(test_list))

res = 0
for idx in range(0, len(test_list)):
	for iidx in range(idx + 1, len(test_list)):

		# checking bidirection
		if test_list[iidx][0] == test_list[idx][1] and test_list[idx][1] == test_list[iidx][0]:
			res += 1

# printing result
print("Bidirectional pairs count : " + str(res))
