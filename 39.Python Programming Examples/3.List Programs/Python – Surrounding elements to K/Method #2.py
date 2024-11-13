# Python3 code to demonstrate working of
# Surrounding elements to K
# Using index() + in operator + loop

# initializing list
test_list = [[7, 6, 3, 2], [5, 6], [2, 1], [6, 1, 2]]

# printing original list
print("The original list is : " + str(test_list))

# initializing K
K = 6

res = []
for sub in test_list:

	# getting index
	# checking for element presence in row
	if K in sub:
		idx = sub.index(K)
	else:
		res.append([])
		continue

	# appending Surrounding elements
	if idx != 0 and idx != len(sub) - 1:
		res.append([sub[idx - 1], sub[idx + 1]])
	elif idx == 0:
		res.append([sub[idx + 1]])
	else:
		res.append([sub[idx - 1]])

# printing result
print("The Surrounding elements : " + str(res))
