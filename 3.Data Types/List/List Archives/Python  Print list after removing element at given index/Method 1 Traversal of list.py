# Python3 program to remove the index
# element from the list
# using traversal

def remove(list1, pos):
    newlist = []

    # traverse in the list
    for x in range(len(list1)):

        # if index not equal to pos
        if x != pos:
            newlist.append(list1[x])
    print(*newlist)


# driver code
list1 = [10, 20, 30, 40, 50]
pos = 2
remove(list1, pos)
