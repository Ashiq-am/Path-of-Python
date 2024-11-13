# Python3 program to extract first and last
# element of each sublist in a list of lists

def Extract(lst):
    return [item[-1] for item in lst]


# Driver code
lst = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
print(Extract(lst))
