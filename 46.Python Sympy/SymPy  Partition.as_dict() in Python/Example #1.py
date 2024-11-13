# Python code explaining
# SymPy.as_dict()

# importing SymPy libraries

from sympy.utilities.iterables import default_sort_key
from sympy.combinatorics.partitions import Partition
from sympy.abc import x, y
from sympy.combinatorics.partitions import IntegerPartition

# Using from sympy.combinatorics.partitions.Partition.as_dict() method
IntegerPartition([11]*3 + [342] + [13]*4).as_dict()
