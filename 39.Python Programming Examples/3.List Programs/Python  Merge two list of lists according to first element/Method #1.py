# Python3 program to Merge two list of
# lists according to first element

def merge(lst1, lst2):
    return [a + [b[1]] for (a, b) in zip(lst1, lst2)]


# Driver code
lst1 = [[1, 'Alice'], [2, 'Bob'], [3, 'Cara']]
lst2 = [[1, 'Delhi'], [2, 'Mumbai'], [3, 'Chennai']]
print(merge(lst1, lst2))
