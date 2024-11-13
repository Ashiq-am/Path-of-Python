# Python3 code to demonstrate
# Interleaving two strings
# using join() + zip() + chain.from_iterable()
from itertools import chain

# initializing strings
test_string1 = 'geeksforgeeks'
test_string2 = 'computerfreak'

# printing original strings
print("The original string 1 : " + test_string1)
print("The original string 2 : " + test_string2)

# using join() + zip() + chain.from_iterable()
# Interleaving two strings
res = "".join(list(chain.from_iterable(zip(test_string1, test_string2))))

# print result
print("The Interleaved string : " + str(res))
