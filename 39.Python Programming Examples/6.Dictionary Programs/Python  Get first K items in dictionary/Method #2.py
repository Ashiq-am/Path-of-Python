# Python3 code to demonstrate working of
# Get first K items in dictionary
# Using islice() + items()
import itertools

# Initialize dictionary
test_dict = {'gfg': 1, 'is': 2, 'best': 3, 'for': 4, 'CS': 5}

# printing original dictionary
print("The original dictionary : " + str(test_dict))

# Initialize limit
K = 3

# Using islice() + items()
# Get first K items in dictionary
res = dict(itertools.islice(test_dict.items(), K))

# printing result
print("Dictionary limited by K is : " + str(res))
