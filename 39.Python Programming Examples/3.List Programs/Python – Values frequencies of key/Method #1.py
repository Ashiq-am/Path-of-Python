# Python3 code to demonstrate working of
# Values frequencies of key
# Using Counter() + list comprehension
from collections import Counter

# initializing list
test_list = [{'gfg' : [1, 5, 6, 7], 'is' : [9, 6, 2, 10]},
			{'gfg' : [5, 6, 7, 8], 'good' : [5, 7, 10]},
			{'gfg' : [7, 5], 'best' : [5, 7]}]

# printing original list
print("The original list is : " + str(test_list))

# frequency key
freq_key = "gfg"

# Values frequencies of key
# Using Counter() + list comprehension
res = Counter([idx for val in test_list for idx in val[freq_key]])

# printing result
print("The frequency dictionary : " + str(dict(res)))
