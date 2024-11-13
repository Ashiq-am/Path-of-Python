# Python program to print all
# sublist from a given list

# function to generate all the sub lists
def sub_lists(l):
    base = []
    lists = [base]
    for i in range(len(l)):
        orig = lists[:]
        new = l[i]
        for j in range(len(lists)):
            lists[j] = lists[j] + [new]
        lists = orig + lists

    return lists


# driver code
l1 = [1, 2, 3]
print(sub_lists(l1))
