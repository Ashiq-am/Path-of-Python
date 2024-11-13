# Python3 code to demonstrate
# to convert list of string and characters
# to list of characters
# using chain.from_iterable()
from itertools import chain

# initializing list
test_list = [ 'gfg', 'i', 's', 'be', 's', 't']

# printing original list
print ("The original list is : " + str(test_list))

# using chain.from_iterable()
# to convert list of string and characters
# to list of characters
res = list(chain.from_iterable(test_list))

# printing result
print ("The list after conversion is : " + str(res))
