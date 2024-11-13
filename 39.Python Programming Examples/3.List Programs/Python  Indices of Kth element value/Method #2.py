# Python3 code to demonstrate working of
# Indices of Kth element value
# Using enumerate() + list comprehension

# initialize list
test_list = [(3, 1, 5), (1, 3, 6), (2, 5, 7),
						(5, 2, 8), (6, 3, 0)]

# printing original list
print("The original list is : " + str(test_list))

# initialize ele
ele = 3

# initialize K
K = 1

# Indices of Kth element value
# Using enumerate() + list comprehension
res = [a for a, b in enumerate(test_list) if b[K] == ele]

# printing result
print("The indices of element at Kth position : " + str(res))
