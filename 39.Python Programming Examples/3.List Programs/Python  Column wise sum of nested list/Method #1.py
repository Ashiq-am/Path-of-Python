# Python3 program to Column wise sum of nested list

def column_sum(lst):
    return [sum(i) for i in zip(*lst)]


# Driver code
lst = [[1, 5, 3], [2, 7, 8], [4, 6, 9]]
print(column_sum(lst))
