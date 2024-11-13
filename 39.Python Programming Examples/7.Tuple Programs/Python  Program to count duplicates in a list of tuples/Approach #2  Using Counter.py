# Python3 code to convert tuple
# into string
import collections


def count(listOfTuple):
    flag = False
    val = collections.Counter(listOfTuple)
    uniqueList = list(set(listOfTuple))

    for i in uniqueList:
        if val[i] >= 2:
            flag = True
            print(i, "-", val[i])

    if flag == False:
        print("Duplicate doesn't exist")

    # Driver code


listOfTuple = [('a', 'e'), ('b', 'x'), ('b', 'x'),
               ('a', 'e'), ('b', 'x')]
count(listOfTuple)
