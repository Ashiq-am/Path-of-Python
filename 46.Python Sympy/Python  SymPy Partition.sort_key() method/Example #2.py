# Python code explaining
# SymPy.sort_key()

# importing SymPy libraries

from sympy.utilities.iterables import default_sort_key
from sympy.combinatorics.partitions import Partition
from sympy.abc import x, y

# Using from sympy.combinatorics.partitions.Partition.sort_key() method

k = Partition([44, x, y])
s = Partition([3, 55, 12, 4])

lst = [k, s]
lst.sort(key = default_sort_key); lst
