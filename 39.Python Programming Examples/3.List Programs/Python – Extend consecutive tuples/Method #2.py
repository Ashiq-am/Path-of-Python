# Python3 code to demonstrate working of
# Extend consecutive tuples
# Using zip() + list comprehension

# initializing list
test_list = [(3, 5, 6, 7), (3, 2, 4, 3), (9, 4), (2, 3, 2), (3,), (3, 6)]

# printing original list
print("The original list is : " + str(test_list))

# zip to combine consecutive elements
res = [a + b for a, b in zip(test_list, test_list[1:])]

# printing results
print("Joined tuples : " + str(res))
