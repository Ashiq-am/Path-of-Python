# Python3 code to demonstrate working of
# Test for Word construction from character list
# Using Counter()
from collections import Counter

# initializing list
test_list = ['g', 'g', 'e', 'k', 's', '4', 'g',
			'g', 'e', 's', 'e', 'e', '4', 'k']

# printing original list
print("The original list is : " + str(test_list))

# initializing string
test_str = 'geeks4geeks'

# cheking for frequency of chars less than in list
res = not bool(dict(Counter(test_str) - Counter(test_list)))

# printing result
print("Is word construction possible ? : " + str(res))
