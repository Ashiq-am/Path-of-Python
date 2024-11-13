# Python3 code to demonstrate
# Merge Consecutive digits Strings
# using list comprehension + groupby() + isdigit()
from itertools import groupby

# Initializing list
test_list = ['gfg', '1', '2', 'is', '5', 'best', '6', '7']

# printing original list
print("The original list is : " + str(test_list))

# Merge Consecutive digits Strings
# using list comprehension + groupby() + isdigit()
res = [sub for i, j in groupby(test_list, str.isdigit) for sub in ([''.join(j)] if i else j)]

# printing result
print ("List after digit merge : " + str(res))
