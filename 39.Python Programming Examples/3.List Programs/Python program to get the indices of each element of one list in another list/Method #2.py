# Python3 code to demonstrate working of
# Multiple Indices from list elements
# Using list comprehension + enumerate()

# initializing list
test_list = [4, 5, 3, 7, 8, 3, 2, 4, 3, 5, 8, 3]

# printing original list
print("The original list is : " + str(test_list))

# initializing get_list
get_list = [7, 5, 3]

# enumerate() used to get idx, val simultaneously
res = [([idx for idx, val in enumerate(test_list) if val == sub] if sub in test_list else [None])
	for sub in get_list]

# printing result
print("Indices of elements in list 1 : " + str(res))
