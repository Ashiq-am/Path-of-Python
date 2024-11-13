# Python3 code to demonstrate working of
# Remove Elements in K distance with N
# Using filter() + lambda

# initializing list
test_list = [4, 5, 9, 1, 10, 6, 13 ]

# printing original list
print("The original list is : " + str(test_list))

# initializing K
K = 3

# initializing N
N = 5

# checking for elements in safe zone with respect to N
res = list(filter(lambda ele : ele < N - K or ele > N + K, test_list))

# printing result
print("Filtered elements : " + str(res))
