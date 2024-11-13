# Python3 code to demonstrate working of
# Dictionary construction from front-rear key values
# Using loop

# initializing list
test_list = [4, 6, 3, 10, 5, 3]

# printing original list
print("The original list : " + str(test_list))


# initializing size and empty Dictionary
n = len(test_list)
res = dict()

# running loop till mid
for idx in range(n // 2):

	# mapping as required
	res.__setitem__(test_list[idx], test_list[n - idx - 1])

# printing result
print("The mapped dictionary : " + str(res))
