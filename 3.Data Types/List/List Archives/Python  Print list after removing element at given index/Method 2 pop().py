# Python3 program to remove the index
# element from the list
# using pop()

def remove(list1, pos):
    # pop the element at index = pos
    list1.pop(pos)
    print(*list1)


# driver code
list1 = [10, 20, 30, 40, 50]
pos = 2
remove(list1, pos)
