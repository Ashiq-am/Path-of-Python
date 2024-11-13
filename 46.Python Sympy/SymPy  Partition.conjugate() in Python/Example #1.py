# Python code explaining
# SymPy.conjugate()

# importing SymPy libraries
from sympy.combinatorics.partitions import Partition
from sympy.combinatorics.partitions import IntegerPartition

# Using from sympy.combinatorics.partitions.Partition.conjugate() method
p = IntegerPartition([312, 14, 23])
print ('Conjugate : ', p.conjugate)
