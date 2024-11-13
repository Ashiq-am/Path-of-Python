# Python3 code to demonstrate working of
# Even elements span in list
# Using list comprehension

# initializing Matrix
test_list = [1, 3, 7, 4, 7, 2, 9, 1, 10, 11]

# printing original list
print("The original list is : " + str(test_list))

# getting even indices
indices_list = [idx for idx in range(
	len(test_list)) if test_list[idx] % 2 == 0]

# getting difference of first and last occurrence
res = indices_list[-1] - indices_list[0]

# printing result
print("Even elements span : " + str(res))
