# Python3 Program to Check is a nested
# list is a subset of another nested list

def checkSubset(list1, list2):
    temp1 = []
    temp2 = []
    for i in list1:
        temp1.append(tuple(i))
    for i in list2:
        temp2.append(tuple(i))

    return set(temp2) < set(temp1)


# Driver Code
list1 = [[2, 3, 1], [4, 5], [6, 8]]
list2 = [[4, 5], [6, 8]]
print(checkSubset(list1, list2))
