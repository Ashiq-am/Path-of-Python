# Python code explaining
# SymPy.conjugate()

# importing SymPy libraries
from sympy.combinatorics.partitions import Partition
from sympy.combinatorics.partitions import IntegerPartition

# Using from sympy.combinatorics.partitions.Partition.conjugate() method

# Only positive elements are required
# so this will generate error
p = IntegerPartition([312, 14, -10, 23, -1])
print ('Conjugate : ', p.conjugate)
