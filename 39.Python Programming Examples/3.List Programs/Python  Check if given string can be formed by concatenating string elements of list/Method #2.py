# Python3 program to Check if given string can
# be formed by concatenating string elements
# of list
import re


def checkList(str, lst):
    r = re.compile("(?:" + "|".join(lst) + ")*$")
    if r.match(str) != None:
        return True

    return False


# Driver code
str = 'geeks'
lst = ['for', 'ge', 'abc', 'ks', 'e']
print(checkList(str, lst))
