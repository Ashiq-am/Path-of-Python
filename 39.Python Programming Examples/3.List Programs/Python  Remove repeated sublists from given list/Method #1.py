# Python3 program to Remove repeated
# unordered sublists from list

def Remove(lst):
    return ([list(i) for i in {*[tuple(sorted(i)) for i in lst]}])


# Driver code
lst = [[1], [1, 2], [3, 4, 5], [2, 1]]
print(Remove(lst))
