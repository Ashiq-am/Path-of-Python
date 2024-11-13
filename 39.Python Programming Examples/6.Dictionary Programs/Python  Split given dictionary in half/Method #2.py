# Python3 code to demonstrate working of
# Split dictionary by half
# Using items() + len() + slice()
from itertools import islice

# Initialize dictionary
test_dict = {'gfg' : 6, 'is' : 4, 'for' : 2, 'CS' : 10}

# printing original dictionary
print("The original dictionary : " + str(test_dict))

# Using items() + len() + slice()
# Split dictionary by half
inc = iter(test_dict.items())
res1 = dict(islice(inc, len(test_dict) // 2))
res2 = dict(inc)

# printing result
print("The first half of dictionary : " + str(res1))
print("The second half of dictionary : " + str(res2))
