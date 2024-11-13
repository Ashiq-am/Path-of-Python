# Python3 code to demonstrate working of
# Convert Character Matrix to single String
# Using join() + chain()
from itertools import chain

# initializing list
test_list = [['g', 'f', 'g'], ['i', 's'], ['b', 'e', 's', 't']]

# printing original list
print("The original list is : " + str(test_list))

# Convert Character Matrix to single String
# Using join() + chain()
res = "".join(chain(*test_list))

# printing result
print("The String after join : " + res)
