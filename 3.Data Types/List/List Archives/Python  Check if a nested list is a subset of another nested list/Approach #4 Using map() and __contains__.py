# Python3 Program to Check is a nested
# list is a subset of another nested list

def checkSubset(list1, list2):
    return all(map(list1.__contains__, list2))


# Driver Code
list1 = [[2, 3, 1], [4, 5], [6, 8]]
list2 = [[4, 5], [6, 8]]
print(checkSubset(list1, list2))
