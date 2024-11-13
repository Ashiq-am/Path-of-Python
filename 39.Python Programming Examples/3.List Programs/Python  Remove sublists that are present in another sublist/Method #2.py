# Python3 program to remove sublists from
# list of lists that are in another sublist
from collections import OrderedDict


def removeSublist(lst):
    curr_result = []
    result = []
    for ele in sorted(map(OrderedDict.fromkeys, lst), key=len, reverse=True):
        if not any(ele.keys() <= req.keys() for req in curr_result):
            curr_result.append(ele)
            result.append(list(ele))

    return result


# Driver code
lst = [['a', 'b', 'c'], ['a', 'b'], ['a', 'b', 'c'], ['d']]
print(removeSublist(lst))
