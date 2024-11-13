# Python3 program to Divide list of strings
# into sublists based on string length
from collections import defaultdict


def divideList(lst):
    group_by_len = defaultdict(list)
    for ele in lst:
        group_by_len[len(ele)].append(ele)

    res = []
    for key in sorted(group_by_len):
        res.append(group_by_len[key])

    return res


# Driver code
lst = ['The', 'art', 'of', 'programming']
print(divideList(lst))
