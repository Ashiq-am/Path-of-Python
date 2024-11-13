# Python3 code to demonstrate working of
# Subtract K from tuples list
# Using list comprehension

# initialize list
test_list = [(1, 3, 4), (2, 4, 6), (3, 8, 1)]

# printing original list
print("The original list : " + str(test_list))

# initialize add element
K = 4

# Subtract K from tuples list
# Using list comprehension
res = [tuple(j - K for j in sub ) for sub in test_list]

# printing result
print("List after subtraction of K : " + str(res))
