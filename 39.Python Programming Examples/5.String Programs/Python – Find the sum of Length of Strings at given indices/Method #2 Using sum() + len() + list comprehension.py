# Python3 code to demonstrate working of
# Length sum of custom indices Strings
# Using sum() + len() + list comprehension

# initializing list
test_list = ["gfg", "is", "best", "for", "geeks"]

# printing original lists
print("The original list is : " + str(test_list))

# initializing idx list
idx_list = [0, 1, 4]

# performing summation using sum()
# len() used to get strings lengths
res = sum([len(ele) for idx, ele in enumerate(test_list) if idx in idx_list])

# printing result
print("Computed Strings lengths sum : " + str(res))
