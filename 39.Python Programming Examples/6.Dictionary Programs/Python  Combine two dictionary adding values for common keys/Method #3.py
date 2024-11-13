# Python program to combine two dictionary
# adding values for common keys
import itertools
import collections

# initializing two dictionaries
dict1 = {'a': 12, 'for': 25, 'c': 9}
dict2 = {'Geeks': 100, 'geek': 200, 'for': 300}

# using defaultdict
Cdict = collections.defaultdict(int)

# iterating key, val with chain()
for key, val in itertools.chain(dict1.items(), dict2.items()):
    Cdict[key] += val

print(dict(Cdict))
