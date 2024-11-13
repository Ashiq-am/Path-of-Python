# Python3 code to demonstrate working of
# Maximum N repeated Elements
# Using loop + count()

# initializing list
test_list = [5, 7, 7, 2, 5, 5, 7, 2, 2]

# printing original list
print("The original list : " + str(test_list))

# initializing N
N = 2

# Using loop + count()
res = []
for ele in test_list:

	# checking of elements occurrence is not greater than N
	if res.count(ele) < N:
		res.append(ele)

# printing result
print("Extracted elements : " + str(res))
