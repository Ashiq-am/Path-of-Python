# Python code explaining
# SymPy.RGS_rank()

# importing SymPy libraries
from sympy.combinatorics.partitions import Partition
from sympy.combinatorics.partitions import RGS_rank

# Using from sympy.combinatorics.partitions.Partition.RGS_rank() method
p = RGS_rank( [0, 0, 0, 0, 0, 1, 1, 1, 0, 1])

print ("rank for restricted growth string : \n", p)
