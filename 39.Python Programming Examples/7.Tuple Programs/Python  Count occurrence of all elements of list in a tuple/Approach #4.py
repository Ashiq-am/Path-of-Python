# Python3 Program to count occurrence
# of all elements of list in a tuple

def countOccurrence(tup, lst):
    dct = {}
    for i in tup:
        if not dct.get(i):
            dct[i] = 0
        dct[i] += 1
    return sum(dct.get(i, 0) for i in lst)


# Driver Code
tup = ('a', 'a', 'c', 'b', 'd')
lst = ['a', 'b']
print(countOccurrence(tup, lst))
