# Python3 code to demonstrate
# Multiplying Alternate elements in List
# using list comprehension + list slicing

# getting Product
def prod(val) :
	res = 1
	for ele in val:
		res *= ele
	return res

# initializing list
test_list = [2, 1, 5, 6, 8, 10]

# printing original list
print("The original list : " + str(test_list))

# using list comprehension + list slicing
# Multiplying Alternate elements in List
res = [prod(test_list[i : : 2]) for i in range(len(test_list) // (len(test_list)//2))]

# print result
print("The alternate elements product list : " + str(res))
