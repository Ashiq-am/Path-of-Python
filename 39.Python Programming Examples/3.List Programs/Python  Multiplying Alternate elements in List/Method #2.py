# Python3 code to demonstrate
# Multiplying Alternate elements in List
# using loop

# initializing list
test_list = [2, 1, 5, 6, 8, 10]

# printing original list
print("The original list : " + str(test_list))

# using loop
# Multiplying Alternate elements in List
res = [1, 1]
for i in range(0, len(test_list)):
	if(i % 2):
		res[1] *= test_list[i]
	else :
		res[0] *= test_list[i]

# print result
print("The alternate elements product list : " + str(res))
