# Python3 code to demonstrate working of
# Extract dictionary keys in Strings List
# Using list comprehension

# initializing list
test_list = ["GeeksforGeeks is best for geeks", "I love GeeksforGeeks"]

# printing original list
print("The original list is : " + str(test_list))

# initializing dictionary
test_dict = {'Geeks': 5, 'CS': 6, 'best': 7, 'love': 10}

# Extract dictionary keys in Strings List
# Using list comprehension
res = [ele if len(ele) > 0 else [None] for ele in [[key for key in test_dict if key in sub]
                                                   for sub in test_list]]

# printing result
print("The matching keys list : " + str(res))
