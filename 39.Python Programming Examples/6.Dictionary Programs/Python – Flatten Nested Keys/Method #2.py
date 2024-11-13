# Python3 code to demonstrate working of
# Flatten Nested Keys
# Using list comprehension + zip() + itemgetter()
from operator import itemgetter

# initializing list
test_list = [{'Gfg' : 1, 'id' : 1, 'data' : [{'rating' : 7, 'price' : 4},
			{'rating' : 17, 'price' : 8}]},
			{'Gfg' : 1, 'id' : 2, 'data' : [{'rating' : 18, 'price' : 19}]}]

# printing original list
print("The original list is : " + str(test_list))

# initializing base and flatten keys
base_keys = 'Gfg', 'id'
flatten_keys = 'rating', 'price'

# Flatten Nested Keys
# Using list comprehension + zip() + itemgetter()
res = [dict(zip(base_keys + flatten_keys, itemgetter(*base_keys)(sub) + itemgetter(*flatten_keys)(data))) for sub in test_list for data in sub['data']]

# printing result
print("The flattened list : " + str(res))
