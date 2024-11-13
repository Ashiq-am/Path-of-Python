# Python3 code to demonstrate working of
# Test if tuple list has Single element
# Using all() + list comprehension

# initializing list
test_list = [(3, 3, 3), (3, 3), (3, 3, 3), (3, 3)]

# printing original list
print("The original list is : " + str(test_list))

# checking for single element using list comprehension
res = all([all(ele == test_list[0][0] for ele in sub) for sub in test_list])

# printing result
print("Are all elements equal : " + str(res))
