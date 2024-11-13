# Python3 code to demonstrate working of
# Subtract K from tuples list
# Using list comprehension + map() + lambda

# initialize list
test_list = [(1, 3, 4), (2, 4, 6), (3, 8, 1)]

# printing original list
print("The original list : " + str(test_list))

# initialize add element
K = 4

# Subtract K from tuples list
# Using list comprehension + map() + lambda
res = [tuple(map(lambda ele : ele - K, sub)) for sub in test_list]

# printing result
print("List after subtraction of K : " + str(res))
