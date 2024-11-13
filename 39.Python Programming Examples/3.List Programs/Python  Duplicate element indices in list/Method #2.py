# Python3 code to demonstrate working of
# Duplicate element indices in list
# Using list comprehension + list slicing

# initializing list
test_list = [1, 4, 5, 5, 5, 9, 1]

# printing original list
print("The original list is : " + str(test_list))

# Duplicate element indices in list
# Using list comprehension + list slicing
res = [idx for idx, val in enumerate(test_list) if val in test_list[:idx]]

# printing result
print("The list of duplicate elements is : " + str(res))
