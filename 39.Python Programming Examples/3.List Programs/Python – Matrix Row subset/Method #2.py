# Python3 code to demonstrate working of
# Matrix Row subset
# Using product() + set() + list comprehension
import itertools

# initializing lists
test_list = [[4, 5, 7], [2, 3, 4], [9, 8, 0]]

# printing original list
print("The original list is : " + str(test_list))

# initializing check Matrix
check_matr = [[2, 3], [1, 2], [9, 0]]

# Matrix Row subset
# Using product() + set() + list comprehension
res = [a for a, b in itertools.product(check_matr, test_list)
										if set(a) <= set(b)]

# printing result
print("Matrix row subsets : " + str(res))
