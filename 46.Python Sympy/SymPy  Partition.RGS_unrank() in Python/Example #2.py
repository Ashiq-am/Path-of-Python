# Python code explaining
# SymPy.RGS_unrank()

# importing SymPy libraries
from sympy.combinatorics.partitions import Partition
from sympy.combinatorics.partitions import RGS_unrank

# Using from sympy.combinatorics.partitions.Partition.RGS_unrank() method
p = RGS_unrank(100, 10)

print ("unranked restricted growth string for super size 10 : \n", p)
