# Python3 code to demonstrate working of
# Construct n*m Matrix from List
# Using loop

# initializing list
test_list = [6, 3, 7, 2, 6, 8, 4, 3, 9, 2, 1, 3]

# printing original list
print("The original list is : " + str(test_list))

# initializing n, m
n, m = 3, 4

k = 0
res = []
if n*m != len(test_list):

	# checking if Matrix Possible
	res = "Matrix Not Possible"
else:

	# Constructing Matrix
	for idx in range(0, n):
		sub = []
		for jdx in range(0, m):
			sub.append(test_list[k])
			k += 1
		res.append(sub)

# printing result
print("Constructed Matrix : " + str(res))
