# import Counter from collections
from collections import Counter

# creating a raw data-set
x = Counter ("geeksforgeeks")

# will return a itertools chain object
# which is basically a pseudo iterable container whose
# elements can be used when called with a iterable tool
print(x.elements())
