# Python3 code to demonstrate
# Valid Ranges Product
# Using loops

# initializing list
test_list = [4, 9, 0, 0, 3, 4, 5, 0, 0, 4, 0]

# printing original list
print("The original list : " + str(test_list))

# using loops
# Valid Ranges Product
res = []
val = 1
for ele in test_list:
	if ele == 0:
		if val != 1:
			res.append(val)
			val = 1
	else:
		val *= ele

# print result
print("The non-zero group product of list is : " + str(res))
