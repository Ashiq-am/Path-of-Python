# Python3 code to demonstrate working of
# Selective Keys Summation
# Using itemgetter() + sum()
from operator import itemgetter

# Initialize dictionary
test_dict = {'gfg': 1, 'is': 2, 'best': 3, 'for': 4, 'CS': 5}

# printing original dictionary
print("The original dictionary : " + str(test_dict))

# Initialize key list
key_list = ['gfg', 'best', 'CS']

# Using itemgetter() + sum()
# Selective Keys Summation
res = sum(list(itemgetter(*key_list)(test_dict)))

# printing result
print("The summation of Selective keys : " + str(res))
