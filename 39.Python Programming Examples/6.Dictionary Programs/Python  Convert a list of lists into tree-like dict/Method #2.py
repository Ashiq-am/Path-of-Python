# Python3 program to Convert a list
# of lists into Dictionary (Tree form)

from functools import reduce
from operator import getitem


def getTree(tree, mappings):
    return reduce(getitem, mappings, tree)


def setTree(tree, mappings):
    getTree(tree, mappings[:-1])[mappings[-1]] = dict()


# Driver Code
lst = [['A'], ['B', 'A'], ['C', 'A'], ['D', 'C', 'A']]
tree = {}
for item in lst:
    setTree(tree, item[::-1])

print(tree)
