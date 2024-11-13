# Python program to get
# dictionary keys as list
from operator import itemgetter


def getList(dict):
    return list(map(itemgetter(0), dict.items()))


# Driver program
dict = {'a': 'Geeks', 'b': 'For', 'c': 'geeks'}
print(getList(dict))
