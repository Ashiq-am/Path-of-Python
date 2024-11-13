# Python3 program to remove sublists from
# list of lists that are in another sublist

def removeSublist(lst):
    curr_res = []
    result = []
    for ele in sorted(map(set, lst), key=len, reverse=True):
        if not any(ele <= req for req in curr_res):
            curr_res.append(ele)
            result.append(list(ele))

    return result


# Driver code
lst = [['a', 'b', 'c'], ['a', 'b'], ['a', 'b', 'c'], ['d']]
print(removeSublist(lst))
