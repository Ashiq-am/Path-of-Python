# Python3 code to demonstrate working of
# Get values of particular key in list of dictionaries
# Using map() + itemgetter()
from operator import itemgetter

# initializing list
test_list = [{'gfg' : 1, 'is' : 2, 'good' : 3},
			{'gfg' : 2}, {'best' : 3, 'gfg' : 4}]

# printing original list
print("The original list is : " + str(test_list))

# Using map() + itemgetter()
# Get values of particular key in list of dictionaries
res = list(map(itemgetter('gfg'), test_list))

# printing result
print("The values corresponding to key : " + str(res))
