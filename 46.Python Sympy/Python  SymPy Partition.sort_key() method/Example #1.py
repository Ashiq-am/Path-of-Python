# Python code explaining
# SymPy.sort_key()

# importing SymPy libraries

from sympy.utilities.iterables import default_sort_key
from sympy.combinatorics.partitions import Partition
from sympy.abc import x

# Using from sympy.combinatorics.partitions.Partition.sort_key() method
g = Partition([134, 322])
e = Partition(list(range(3)))
k = Partition([44, x])
s = Partition([3, 4])

lst = [s, k, g + 1, k, e]
lst.sort(key = default_sort_key); lst
