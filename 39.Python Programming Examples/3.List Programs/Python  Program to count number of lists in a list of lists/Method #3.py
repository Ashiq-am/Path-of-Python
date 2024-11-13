# Python3 program to Count number
# of lists in a list of lists

def countList(lst):
    return sum(isinstance(i, list) for i in lst)


# Driver code
lst = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
print(countList(lst))
