import sys

dict = {}
print(dict)

# We will get size of empty dict
print(sys.getsizeof(dict))

t1 = ()
d = list(t1)
print(d)

# We will get size of empty list of tuples
print(sys.getsizeof(d))
