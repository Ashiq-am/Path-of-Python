# Python program to get N key:value pairs in given dictionary
# using list slicing

# Initialize dictionary
test_dict = {'Geeks': 1, 'For': 2, 'is': 3, 'best': 4, 'for': 5, 'CS': 6}

# printing original dictionary
print("The original dictionary : " + str(test_dict))

# Initialize limit
N = 3

# Using items() + list slicing
# Get first K items in dictionary
out = dict(list(test_dict.items())[0: N])

# printing result
print("Dictionary limited by K is : " + str(out))
