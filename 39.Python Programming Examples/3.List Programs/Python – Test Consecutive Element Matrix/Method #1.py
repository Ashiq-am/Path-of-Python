# Python3 code to demonstrate working of
# Test Consecutive Element Matrix
# Using loop

# initializing list
test_list = [[4, 5, 6], [7], [8, 9, 10], [11, 12]]

# printing original list
print("The original list is : " + str(test_list))

res = True
mem_list = []
for sub in test_list:
	flag = True
	for ele in sub:

		# checking for last element to be Consecutive
		if len(mem_list) != 0:
			if mem_list[-1] != ele - 1:
				flag = False
				break
		mem_list.append(ele)

	if not flag:
		res = False
		break

# printing result
print("Is Matrix Consecutive ? : " + str(res))
