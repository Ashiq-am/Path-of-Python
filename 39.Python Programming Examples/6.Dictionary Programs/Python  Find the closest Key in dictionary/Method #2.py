# Python3 code to demonstrate working of
# Closest key in dictionary
# Using bisect_left() + OrderedDict()
import collections
import bisect

# initializing dictionary
test_dict = collections.OrderedDict()
test_dict = {13 : 'Hi', 15 : 'Hello', 16 : 'Gfg'}

# initializing nearest key
search_key = 15.6

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

# Using bisect_left() + OrderedDict()
# Closest key in dictionary
res = bisect.bisect_left(list(test_dict.keys()), 15.6)

# printing result
print("The position of closest key : " + str(res))
