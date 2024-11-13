# Python3 code to Concatenate
# corresponding sublists from two
# different lists
from operator import concat


def concatList(l1, l2):
    return [list(map(concat, i, j)) for i, j in zip(l1, l2)]


# Driver Code
l1 = [['1', '2'], ['1', '2', '3']]
l2 = [['anne', 'bob'], ['cara', 'drake', 'ezra']]
print(concatList(l1, l2))
