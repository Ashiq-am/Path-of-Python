# python program to extend a list using
# "chain" iterator functions
from itertools import *

a = [10, 20, 30]

# extend a list
print(list(chain(a, [40, 50, 60])))
