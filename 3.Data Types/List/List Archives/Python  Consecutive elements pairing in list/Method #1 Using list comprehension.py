# Python3 code to demonstrate
# consecutive element pairing
# using list comprehension

# initializing list
test_list = [5, 4, 1, 3, 2]

# printing original list
print("The original list : " + str(test_list))

# using list comprehension
# consecutive element pairing
res = [[test_list[i], test_list[i + 1]]
		for i in range(len(test_list) - 1)]

# print result
print("The consecutive element paired list is : " + str(res))
