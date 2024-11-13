# Python3 Program to Check is a nested
# list is a subset of another nested list

def checkSubset(list1, list2):
    l1, l2 = list1[0], list2[0]
    exist = True
    for i in list2:
        if i not in list1:
            exist = False
    return exist


# Driver Code
list1 = [[2, 3, 1], [4, 5], [6, 8]]
list2 = [[4, 5], [6, 8]]
print(checkSubset(list1, list2))
