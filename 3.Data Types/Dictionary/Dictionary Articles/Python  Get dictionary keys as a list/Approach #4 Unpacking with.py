# Python program to get
# dictionary keys as list

def getList(dict):
    return [*dict]


# Driver program
dict = {'a': 'Geeks', 'b': 'For', 'c': 'geeks'}
print(getList(dict))
