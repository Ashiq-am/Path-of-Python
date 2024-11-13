# Python3 program to print diagonals in 2D list

def printDiagnol(lst):
    # To print Primary Diagnol
    print('Diagnol 1 - ', end="")
    print([lst[i][i] for i in range(len(lst))])

    # To print Secondry Diagnol
    print('Diagnol 2 - ', end="")
    print([lst[i][len(lst) - i - 1] for i in range(len(lst))])


# Driver code
lst = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
printDiagnol(lst)
