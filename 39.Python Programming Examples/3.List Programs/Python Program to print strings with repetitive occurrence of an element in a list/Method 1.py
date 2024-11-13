# initializing Matrix
test_list = ["geeksforgeeks", "best", "for", "geeks"]

# printing original list
print("The original list is : " + str(test_list))

# initializing K
K = 'e'

res = []
for ele in test_list:

	# checking for count greater than 1 (repetitive)
	if ele.count(K) > 1:
		res.append(ele)

# printing result
print("Repeated K strings : " + str(res))
