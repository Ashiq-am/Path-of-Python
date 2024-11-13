# Python3 program to print diagonals in 2D list

def printDiagnol(lst):
    # To print Primary Diagnol
    print('Diagnol 1 - ', end="")
    print([r[i] for i, r in enumerate(lst)])

    # To print Secondary Diagnol
    print('Diagnol 2 - ', end="")
    print([r[~i] for i, r in enumerate(lst)])


# Driver code
lst = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
printDiagnol(lst)
