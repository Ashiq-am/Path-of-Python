# Python3 code to demonstrate working of
# Even elements span in list
# Using filter() + lambda

# initializing Matrix
test_list = [1, 3, 7, 4, 7, 2, 9, 1, 10, 11]

# printing original list
print("The original list is : " + str(test_list))

# getting even indices
indices_list = list(
	filter(lambda x: test_list[x] % 2 == 0, range(len(test_list))))

# getting difference of first and last occurrence
res = indices_list[-1] - indices_list[0]

# printing result
print("Even elements span : " + str(res))
