# Python3 program to Convert list of
# sequential number into intervals
import itertools


def intervals_extract(iterable):
    iterable = sorted(set(iterable))
    for key, group in itertools.groupby(enumerate(iterable),
                                        lambda t: t[1] - t[0]):
        group = list(group)
        yield [group[0][1], group[-1][1]]

    # Driver code


l = [2, 3, 4, 5, 7, 8, 9, 11, 15, 16]
print(list(intervals_extract(l)))
