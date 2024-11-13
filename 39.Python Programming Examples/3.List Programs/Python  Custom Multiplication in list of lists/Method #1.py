# Python3 code to demonstrate
# Custom Multiplication in list of lists
# Using loops

# initializing list
test_list = [[5, 6, 8], [7, 4, 3], [8, 10, 12]]

# initializing multiply list
mult_list = [10, 20, 30]

# printing original list
print("The original list : " + str(test_list))

# printing multiply list
print("The original multiply list : " + str(mult_list))

# using loops
# Custom Multiplication in list of lists
res = [[] for idx in range(len(test_list))]
for i in range(len(test_list)):
	for j in range(len(mult_list)):
		res[i] += [mult_list[i] * test_list[i][j]]

# print result
print("The list after multiply : " + str(res))
