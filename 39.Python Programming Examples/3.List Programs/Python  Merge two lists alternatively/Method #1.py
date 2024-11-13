# Python3 program to merge two lists
# alternatively

def countList(lst1, lst2):
    return [sub[item] for item in range(len(lst2))
            for sub in [lst1, lst2]]


# Driver code
lst1 = [1, 2, 3]
lst2 = ['a', 'b', 'c']
print(countList(lst1, lst2))
