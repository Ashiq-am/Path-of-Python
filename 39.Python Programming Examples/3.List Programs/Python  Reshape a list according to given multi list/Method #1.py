# Python3 program to reshape a list
# according to multidimensional list

def reshape(lst1, lst2):
    last = 0
    res = []
    for ele in list1:
        res.append(list2[last: last + len(ele)])
        last += len(ele)

    return res


# Driver code
list1 = [[1], [2, 3], [4, 5, 6]]
list2 = ['a', 'b', 'c', 'd', 'e', 'f']
print(reshape(list1, list2))
