# A Python program to demonstrate
# the difference between regular
# and ordered dictionary.


import collections


# Creating a regular dictionary
print('Regular dictionary:')
d = {chr(k):k for k in range(ord('a'), ord('g'))}

for k, v in d.items():
	print(k, v)

# Creating an Ordered dictionary
print('\nOrderedDict:')
d = collections.OrderedDict()
[d.setdefault(chr(k), k) for k in range(ord('a'), ord('g'))]

for k, v in d.items():
	print(k, v)
