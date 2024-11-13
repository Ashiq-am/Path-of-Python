# Python3 program to Find groups
# of strictly increasing numbers within
from itertools import groupby, cycle


def groupSequence(l):
    temp_list = cycle(l)

    next(temp_list)
    groups = groupby(l, key=lambda j: j + 1 == next(temp_list))
    for k, v in groups:
        if k:
            yield tuple(v) + (next((next(groups)[1])),)


# Driver program
l = [8, 9, 10, 7, 8, 1, 2, 3]
print(list(groupSequence(l)))
