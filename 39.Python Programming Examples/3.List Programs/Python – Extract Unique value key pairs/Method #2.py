# Python3 code to demonstrate working of
# Extract Unique value key pairs
# Using map() + zip() + itemgetter()
from operator import itemgetter

# initializing list
test_list = [{'gfg' : 5, 'is' : 8, 'best' : 12},
			{'gfg' : 5, 'is' : 12, 'best' : 12},
			{'gfg' : 15, 'is' : 17, 'best' : 21}]

# printing original list
print("The original list is : " + str(test_list))

# initializing required keys
req_key1 = 'gfg'
req_key2 = 'best'

# Extract Unique value key pairs
# Using map() + zip() + itemgetter()
temp = zip(*map(itemgetter(req_key1, req_key2), test_list))
res = list(map(set, temp))

# printing result
print("The required values : " + str(res))
