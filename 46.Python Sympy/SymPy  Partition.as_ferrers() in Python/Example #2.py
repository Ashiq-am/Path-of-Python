# Python code explaining
# SymPy.as_ferrers()

# importing SymPy libraries
from sympy.combinatorics.partitions import Partition
from sympy.combinatorics.partitions import IntegerPartition

# Using from sympy.combinatorics.partitions.Partition.as_ferrers() method
print(IntegerPartition([1, 2, 3, 4]).as_ferrers(char = '*'))
