# Python code to demonstrate
# Joining unicode list elements
# using join() + list comprehension

# initializing list
from numpy.compat import unicode

test_list = [ 'We', 'love', 'Geeksforgeeks']
map(unicode, test_list)

# printing original list
print("The original list is : " + str(test_list))

# using join() + list comprehension to
# Join unicode list elements
res = b':'.join(str(i) for i in test_list)

# printing result
print ("The joined string is : " + res)
