# Python3 program to Find all distinct
# pairs with difference equal to k

def findPairs(lst, k):
    res = []
    for e in lst:
        if e + k in lst:
            res.append(tuple((e, e + k)))

    return res


# Driver code
lst = [1, 5, 3, 4, 2]
k = 3
print(findPairs(lst, k))
