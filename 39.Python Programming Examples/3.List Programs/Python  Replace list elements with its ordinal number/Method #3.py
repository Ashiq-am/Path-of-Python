# Python3 program to Replace element
# in a list with its ordinal number

def replaceOrdinal(lst):
    return [[idx for _ in sublist]
            for idx, sublist in enumerate(lst)]


# Driver Code
lst = [[1, 2, 3], [4, 5, 6], [7, 8, 9, 10]]
print(replaceOrdinal(lst))
