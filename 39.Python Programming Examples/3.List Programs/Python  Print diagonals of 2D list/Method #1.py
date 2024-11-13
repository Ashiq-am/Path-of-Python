# Python2 program to print diagonals in 2D list

def printDiagnol(lst):
    # To print Primary Diagnol
    print('Diagnol 1 -'),
    print([lst[i][i] for i in xrange(len(lst))])

    # To print Secondry Diagnol
    print('Diagnol 2 -'),
    print([lst[i][len(lst) - 1 - i] for i in xrange(len(lst))])


# Driver code
lst = [[1, 2, 3],
       [4, 5, 6],
       [7, 8, 9]]

printDiagnol(lst)
