# Python3 code to demonstrate working of
# Elements with factors less than K
# Using filter() + lambda + len() + list comprehension


def factors_less_k(ele, K):

	# comparing for factors
	return len([idx for idx in range(1, ele + 1) if ele % idx == 0]) <= K


# initializing list
test_list = [60, 12, 100, 17, 18]

# printing original list
print("The original list is : " + str(test_list))

# initializing K
K = 4

# filtering using filter() + lambda
res = list(filter(lambda ele: factors_less_k(ele, K), test_list))

# printing result
print("Filtered elements : " + str(res))
