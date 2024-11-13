# Python3 code to demonstrate
# summation of non-zero groups
# Using loops

# initializing list
test_list = [4, 9, 0, 0, 3, 4, 5, 0, 0, 4, 0]

# printing original list
print("The original list : " + str(test_list))

# using loops
# summation of non-zero groups
res = []
val = 0
for ele in test_list:
	if ele == 0:
		if val != 0:
			res.append(val)
			val = 0
	else:
		val += ele

# print result
print("The non-zero group summation of list is : " + str(res))
