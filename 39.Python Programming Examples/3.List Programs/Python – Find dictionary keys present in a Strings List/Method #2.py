# Python3 code to demonstrate working of
# Extract dictionary keys in Strings List
# Using filter() + lambda + list comprehension

# initializing list
test_list = ["GeeksforGeeks is best for geeks", "I love GeeksforGeeks"]

# printing original list
print("The original list is : " + str(test_list))

# initializing dictionary
test_dict = {'Geeks': 5, 'CS': 6, 'best': 7, 'love': 10}

# Extract dictionary keys in Strings List
# Using filter() + lambda + list comprehension
res = [list(filter(lambda ele: ele in sub, test_dict)) for sub in test_list]

# printing result
print("The matching keys list : " + str(res))
