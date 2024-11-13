# Python program to combine two dictionary
# adding values for common keys
from collections import Counter

# initializing two dictionaries
dict1 = {'a': 12, 'for': 25, 'c': 9}
dict2 = {'Geeks': 100, 'geek': 200, 'for': 300}

# adding the values with common key

Cdict = Counter(dict1) + Counter(dict2)
print(Cdict)
