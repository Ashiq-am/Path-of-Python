# Python3 code to demonstrate working of
# Retain records of specific length
# Using list comprehension + len()

# Initializing list
test_list = [(4, 5, 6), (5, 6), (2, 3, 5), (5, 6, 8), (5, 9)]

# printing original list
print("The original list is : " + str(test_list))

# Initializing desired length
N = 3

# Retain records of specific length
# Using list comprehension + len()
res = [sub for sub in test_list if len(sub) == 3]

# printing result
print("The tuple list after removing uneven records: " + str(res))
