# Python3 code to demonstrate working of
# Convert nested sublist into tuples
# Using map() + list comprehension + tuple

# Initializing list
test_list = [[[1, 2, 3], [4, 6, 7]], [[6, 9, 8], [10, 11, 12]]]

# printing original list
print("The original list is : " + str(test_list))

# Convert nested sublist into tuples
# Using map() + list comprehension + tuple
res = [list(map(tuple, sub)) for sub in test_list]

# printing result
print("The data after conversion to tuple is : " + str(res))
