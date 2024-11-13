# Python3 program to Remove repeated
# unordered sublists from list

def Remove(lst):
    res = []
    check = set()

    for x in lst:
        hsh = tuple(sorted(x))
        if hsh not in check:
            res.append(x)
            check.add(hsh)

    return res


# Driver code
lst = [[1], [1, 2], [3, 4, 5], [2, 1]]
print(Remove(lst))
