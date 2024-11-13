# Python3 code to demonstrate working of
# Extract Item with Maximum Tuple Value
# Using max() + map() + itemgetter() + zip()
from operator import itemgetter

# initializing dictionary
test_dict = {'gfg' : (4, 6),
			'is' : (7, 8),
			'best' : (8, 2)}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

# initializing tuple index
# 0 based indexing
tup_idx = 1

# Extract Item with Maximum Tuple Value
# Using max() + map() + itemgetter() + zip()
res = max(zip(test_dict.keys(), map(itemgetter(tup_idx), inventory.values())), key = itemgetter(1))[0]
res = (res, test_dict[res])

# printing result
print("The extracted maximum element item : " + str(res))
