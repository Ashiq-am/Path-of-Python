# Python3 code to demonstrate working of
# Elements with factors less than K
# Using list comprehension


def factors_less_k(ele, K):

	# comparing for factors
	return len([idx for idx in range(1, ele + 1) if ele % idx == 0]) <= K


# initializing list
test_list = [60, 12, 100, 17, 18]

# printing original list
print("The original list is : " + str(test_list))

# initializing K
K = 4

# checking for each element
res = [ele for ele in test_list if factors_less_k(ele, K)]

# printing result
print("Filtered elements : " + str(res))
