# Python3 code to demonstrate working of
# Mixed List Integer Multiplication
# using loop + isinstance()

# initializing list
test_list = [5, 8, "gfg", 8, (5, 7), 'is', 2]

# printing original list
print("The original list is : " + str(test_list))

# Mixed List Integer Multiplication
# using loop + isinstance()
res = 1
for ele in test_list:
	if(isinstance(ele, int)):
		res *= ele

# printing result
print("Product of integers in list : " + str(res))
