# Python3 code to demonstrate
# Concatenating Kth element in Tuple List
# using list comprehension

# initializing list of tuples
test_list = [(1, 'Rash', 21), (2, 'Varsha', 20), (3, 'Kil', 19)]

# printing original list
print("The original list is : " + str(test_list))

# initializing K
K = 1

# using list comprehension + join() to concatenate names
res = " ".join([lis[K] for lis in test_list])

# printing result
print("String with only Kth tuple element (i.e names) concatenated : " + str(res))
