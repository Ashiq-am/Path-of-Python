# Python3 code to demonstrate working of
# Values Frequency grouping of K in dictionaries
# Using Counter()
from collections import Counter

# initializing list
test_list = [{'gfg' : 3, 'best' : 4}, {'gfg' : 3, 'best' : 5},
			{'gfg' : 4, 'best' : 4}, {'gfg' : 7, 'best' : 4} ]

# printing original list
print("The original list is : " + str(test_list))

# initializing K
K = 'gfg'

# groupby() used to group values and len() to compute Frequency
res = dict(Counter(sub[K] for sub in test_list))

# printing result
print("The Values Frequency : " + str(res))
