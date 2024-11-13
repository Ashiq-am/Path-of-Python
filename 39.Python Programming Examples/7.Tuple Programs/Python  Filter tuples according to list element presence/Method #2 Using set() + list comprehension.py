# Python3 code to demonstrate working of
# Filter tuples according to list element presence
# using set() + list comprehension

# initialize list of tuple
test_list = [(1, 4, 6), (5, 8), (2, 9), (1, 10)]

# initialize target list
tar_list = [6, 10]

# printing original tuples list
print("The original list : " + str(test_list))

# Filter tuples according to list element presence
# using set() + list comprehension
res = [tup for tup in test_list if (set(tar_list) & set(tup))]

# printing result
print("Filtered tuple from list are : " + str(res))
