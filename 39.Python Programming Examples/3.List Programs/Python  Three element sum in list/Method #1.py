# Python3 code to demonstrate
# 3 element sum
# using nested loops

# initializing list
test_list = [4, 1, 3, 2, 6, 5]

# initializing sum
sum = 9

# printing original list
print("The original list : " + str(test_list))

# using nested loops
# 3 element sum
res = []
for i in range(0, len(test_list)-2):
	for j in range(i + 1, len(test_list)-1):
		for k in range(j + 1, len(test_list)):
			if test_list[i] + test_list[j] + test_list[k] == sum:
				temp = []
				temp.append(test_list[i])
				temp.append(test_list[j])
				temp.append(test_list[k])
				res.append(tuple(temp))

# print result
print("The 3 sum element list is : " + str(res))
