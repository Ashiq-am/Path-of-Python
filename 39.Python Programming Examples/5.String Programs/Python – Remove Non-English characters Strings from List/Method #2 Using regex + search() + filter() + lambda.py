# Python3 code to demonstrate working of
# Remove Non-English characters Strings from List
# Using regex + search() + filter() + lambda
import re

# initializing list
test_list = ['Gfg', 'Good| ????', "for", '??Geeks???']

# printing original list
print("The original list is : " + str(test_list))

# using search() to get only those strings with alphabets
res = list(filter(lambda ele: re.search("[a-zA-Z\s]+", ele) is not None, test_list))

# printing result
print("The extracted list : " + str(res))
