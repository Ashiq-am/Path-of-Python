# Python3 code to Update a list
# of tuples according to another list

from collections import defaultdict


def merge(list1, list2):
    dic = defaultdict(list)
    for i, j in list1 + list2:
        dic[i].append(j)

    return sorted([(i, max(j)) for i, j in dic.items()],
                  key=lambda x: x[0])


# Driver Code
list1 = [('a', 0), ('b', 0), ('c', 0)]
list2 = [('a', 5), ('c', 3)]
print(merge(list1, list2))
