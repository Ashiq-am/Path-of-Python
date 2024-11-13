# Python3 program to Remove repeated
# unordered sublists from list

def Remove(lst):
    return list(map(list, (set(map(lambda x: tuple(sorted(x)), lst)))))


# Driver code
lst = [[1], [1, 2], [3, 4, 5], [2, 1]]
print(Remove(lst))
