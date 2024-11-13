# Python3 program to Count number
# of lists in a list of lists

def countList(lst):
    count = 0
    for el in lst:
        if type(el) == type([]):
            count += 1

    return count


# Driver code
lst = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
print(countList(lst))
