# Python3 code to demonstrate
# Getting K elements after N values
# using list comprehension

# initializing list
test_list = [4, 5, 2, 7, 8, 4, 10, 9, 11, 13]

# printing original list
print("The original list : " + str(test_list))

# initializing N and K
N = 2
K = 3

# using list comprehension
# Getting K elements after N values
res = [y for x in [test_list[i : i + K] for i in
	range(0, len(test_list), N + K)] for y in x]

# print result
print("The list after selective slicing : " + str(res))
