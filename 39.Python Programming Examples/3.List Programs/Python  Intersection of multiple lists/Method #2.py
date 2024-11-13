# Python3 program to find
# Intersection of list of list

def intersection(lst1, lst2):
    tup1 = map(tuple, lst1)
    tup2 = map(tuple, lst2)
    return list(map(list, set(tup1).intersection(tup2)))


# Driver code
lst1 = [['a', 'c'], ['d', 'e']]
lst2 = [['a', 'c'], ['e', 'f'], ['d', 'e']]
print(intersection(lst1, lst2))
