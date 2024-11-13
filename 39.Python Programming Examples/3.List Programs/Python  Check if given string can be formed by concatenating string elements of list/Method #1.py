# Python3 program to Check if given string can
# be formed by concatenating string elements
# of list
from itertools import permutations


def checkList(str, lst):
    for i in range(2, len(lst) + 1):
        for perm in permutations(lst, i):
            if ''.join(perm) == str:
                return True

    return False


# Driver code
str = 'geeks'
lst = ['for', 'ge', 'abc', 'ks', 'e', 'xyz']
print(checkList(str, lst))
