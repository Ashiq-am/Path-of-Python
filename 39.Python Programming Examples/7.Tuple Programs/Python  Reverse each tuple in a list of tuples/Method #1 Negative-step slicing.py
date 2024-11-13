# Python3 program to Reverse
# each tuple in a list of tuples

def reverseTuple(lstOfTuple):
    return [tup[::-1] for tup in lstOfTuple]


# Driver code
lstOfTuple = [(1, 2), (3, 4, 5), (6, 7, 8, 9)]
print(reverseTuple(lstOfTuple))
