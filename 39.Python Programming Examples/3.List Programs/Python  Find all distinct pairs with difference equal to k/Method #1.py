# Python3 program to Find all distinct
# pairs with difference equal to k

def findPairs(lst, k):
    return [(e1, e2) for e1 in lst
            for e2 in lst if (e1 - e2 == k)]


# Driver code
lst = [1, 5, 3, 4, 2]
k = 3
print(findPairs(lst, k))
