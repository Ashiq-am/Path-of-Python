# Python3 code to demonstrate
# Extracting numbers from list of strings
# using join() + isnumeric() + list comprehension + map()

# initializing list
test_list = ['Rs. 24', 'Rs. 18', 'Rs. 8', 'Rs. 21']

# printing original list
print("The original list : " + str(test_list))

# using join() + isnumeric() + list comprehension + map()
# Extracting numbers from list of strings
res = list(map(lambda sub:int(''.join(
	[ele for ele in sub if ele.isnumeric()])), test_list))

# print result
print("The list after Extracting numbers : " + str(res))
