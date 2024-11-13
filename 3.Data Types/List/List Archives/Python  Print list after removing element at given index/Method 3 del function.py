# Python3 program to remove the index element
# from the list using del

def remove(list1, pos):
    # delete the element at index = pos
    del list1[pos]
    print(*list1)


# driver code
list1 = [10, 20, 30, 40, 50]
pos = 2
remove(list1, pos)
