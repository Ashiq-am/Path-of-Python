# Python3 code to demonstrate working of
# Non K distant elements
# Using list comprehension

# initializing list
test_list = [8, 10, 16, 20, 3, 1, 7]

# printing original list
print("The original list is : " + str(test_list))

# initializing K
K = 2

# using list comprehension to get all elements of non K distance
res = [ele for ele in test_list if ele +
	K not in test_list and ele - K not in test_list]

# printing result
print("The filtered List : " + str(res))
