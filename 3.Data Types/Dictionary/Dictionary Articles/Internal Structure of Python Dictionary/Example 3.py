import sys

d = {}
d['a'] = 'a' * 100000
print("Size of dicitonary ->", sys.getsizeof(d))
print("Size of a ->", sys.getsizeof('a'))
