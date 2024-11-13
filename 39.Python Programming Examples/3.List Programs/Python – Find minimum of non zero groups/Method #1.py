# Python3 code to demonstrate
# Natural Numbers Minimum
# Using loops

# initializing list
test_list = [4, 9, 0, 0, 3, 4, 5, 0, 0, 4, 0]

# printing original list
print("The original list : " + str(test_list))

# using loops
# Natural Numbers Minimum
res = []
val = 99999
for ele in test_list:
	if ele == 0:
		if val != 99999:
			res.append(val)
			val = 99999
	else:
		val = min(val, ele)

# print result
print("The non-zero group Minimum of list is : " + str(res))
