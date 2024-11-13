# initializing list
test_list = [4, 3, 5, 6, 9, 16, 11, 10, 12]

# printing original list
print("The original list is : " + str(test_list))

# initializing K
K = 4

res = True
for idx, ele in enumerate(test_list):

	# checking for required conditions
	if (idx > K and ele < test_list[K]) or (idx < K and ele > test_list[K]):
		res = False

# printing result
print("Is condition met ? : " + str(res))
