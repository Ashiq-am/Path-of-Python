# Python program to add the occurrence
# of each number as sublists
def count_occur(list1, **kwargs):
    # iterate over list item
    for i in list1:
        row = []
        ct = 0

        # count function will count occurrence
        ct = list1.count(i)
        row.append(i)
        row.append(ct)
        # append 1d list items to 2d list
        list2.append(row)

    # below code is to eliminate
    # repetitive list items
    for j in list2:
        if j not in unq_l2:
            unq_l2.append(j)

    return unq_l2


# Driver Code
l1 = [3, 5, 7, 2, 3, 5, 9.1]
list2 = []
unq_l2 = []
print(count_occur(l1))
