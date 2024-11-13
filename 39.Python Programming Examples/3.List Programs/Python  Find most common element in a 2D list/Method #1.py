# Python3 program to find most
# common element in a 2D list

def mostCommon(lst):
    flatList = [el for sublist in lst for el in sublist]
    return max(flatList, key=flatList.count)


# Driver code
lst = [[10, 20, 30], [20, 50, 10], [30, 50, 10]]
print(mostCommon(lst))
