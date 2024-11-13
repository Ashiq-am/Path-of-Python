# Python3 code to demonstrate working of
# Summation of Kth Column of Tuple List
# using list comprehension + sum()

# initialize list
test_list = [(5, 6, 7), (1, 3, 5), (8, 9, 19)]

# printing original list
print("The original list is : " + str(test_list))

# initialize K
K = 2

# Summation of Kth Column of Tuple List
# using list comprehension + sum()
res = sum([sub[K] for sub in test_list])

# printing result
print("Summation of Kth Column of Tuple List : " + str(res))
