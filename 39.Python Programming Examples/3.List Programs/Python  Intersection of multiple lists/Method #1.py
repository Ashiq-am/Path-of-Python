# Python3 program to find
# Intersection of list of lists

def intersection(lst1, lst2):
    return [item for item in lst1 if item in lst2]


# Driver code
lst1 = [['a', 'c'], ['d', 'e']]
lst2 = [['a', 'c'], ['e', 'f'], ['d', 'e']]
print(intersection(lst1, lst2))
