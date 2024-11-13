# Python3 program to Replace element
# in a list with its ordinal number

def replaceOrdinal(lst):
    return [[i for j in range(len(lst[i]))]
            for i in range(len(lst))]


# Driver Code
lst = [[1, 2, 3], [4, 5, 6], [7, 8, 9, 10]]
print(replaceOrdinal(lst))
