# initializing list
test_list = [4, 3, 5, 6, 9, 16, 11, 10, 12]

# printing original list
print("The original list is : " + str(test_list))

# initializing K
K = 4

# all() used to check for condition using one liner
res = all(not ((idx > K and ele < test_list[K]) or (
	idx < K and ele > test_list[K])) for idx, ele in enumerate(test_list))

# printing result
print("Is condition met ? : " + str(res))
