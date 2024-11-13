# Python3 code to demonstrate working of
# Mixed List Integer Multiplication
# using type caste and exception handling

# initializing list
test_list = [5, 8, "gfg", 8, (5, 7), 'is', 2]

# printing original list
print("The original list is : " + str(test_list))

# Mixed List Integer Multiplication
# using type caste and exception handling
res = 1
for ele in test_list:
	try:
		res *= int(ele)
	except :
		pass

# printing result
print("Product of integers in list : " + str(res))
