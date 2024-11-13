import numpy


def Sorting(lst):
    # list for storing the length of each string in list
    lenlist = []
    for x in lst:
        lenlist.append(len(x))

    # return a list with the index of the sorted
    # items in the list
    sortedindex = numpy.argsort(lenlist)

    # creating a dummy list where we will place the
    # word according to the sortedindex list
    lst2 = ['dummy'] * len(lst)

    # print(sortedindex,lenlist)
    for i in range(len(lst)):
        # placing element in the lst2 list by taking the
        # value from original list lst where it should belong
        # in the sorted list by taking its index from sortedindex
        lst2[i] = lst[sortedindex[i]]

    return lst2


# Driver code
lst = ["rohan", "amy", "sapna", "muhammad",
       "aakash", "raunak", "chinmoy"]
print(Sorting(lst))
