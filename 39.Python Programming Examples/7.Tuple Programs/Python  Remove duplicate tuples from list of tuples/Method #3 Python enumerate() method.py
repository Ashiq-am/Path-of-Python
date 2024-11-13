# Python3 program to remove duplicate
# tuples from list of tuples

def removeDuplicates(lst):
    return [[a, b] for i, [a, b] in enumerate(lst)
            if not any(c == b for _, c in lst[:i])]


# Driver code
lst = [(1, 2), (5, 7), (3, 6), (1, 2)]
print(removeDuplicates(lst))
