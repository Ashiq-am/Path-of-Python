# Python3 code to demonstrate
# Joining unicode list elements
# using join() + str()

# initializing list
from numpy.compat import unicode

test_list = [ 'We', 'love', 'Geeksforgeeks']
map(unicode, test_list)

# printing original list
print("The original list is : " + str(test_list))

# using join() + str() to
# Join unicode list elements
res = str(u':'.join(test_list))

# printing result
print ("The joined string is : " + res)
