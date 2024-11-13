# Python3 Program to count occurrence
# of all elements of list in a tuple

def countOccurrence(tup, lst):
    lst = set(lst)
    return sum(1 for x in tup if x in lst)


# Driver Code
tup = ('a', 'a', 'c', 'b', 'd')
lst = ['a', 'b']
print(countOccurrence(tup, lst))
