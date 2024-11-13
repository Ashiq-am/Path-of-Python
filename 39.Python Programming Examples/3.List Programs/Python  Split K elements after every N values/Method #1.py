# Python3 code to demonstrate
# Getting K elements after N values
# using loops

# initializing list
test_list = [4, 5, 2, 7, 8, 4, 10, 9, 11, 13]

# printing original list
print("The original list : " + str(test_list))

# initializing N and K
N = 2
K = 3

# using loops
# Getting K elements after N values
res =[]
while test_list:
	res += test_list[:K]
	test_list = test_list[K + N:]

# print result
print("The list after selective slicing : " + str(res))
