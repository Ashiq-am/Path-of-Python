# Python program to get N key:value pairs in given dictionary
# using itertools.islice() method

import itertools

# Initialize dictionary
test_dict = {'Geeks': 1, 'For': 2, 'is': 3, 'best': 4, 'for': 5, 'CS': 6}

# printing original dictionary
print("The original dictionary : " + str(test_dict))

# Initialize limit
N = 3

# Using islice() + items()
# Get first N items in dictionary
out = dict(itertools.islice(test_dict.items(), N))

# printing result
print("Dictionary limited by K is : " + str(out))
