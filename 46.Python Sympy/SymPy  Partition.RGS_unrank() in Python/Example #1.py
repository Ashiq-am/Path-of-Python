# Python code explaining
# SymPy.RGS_unrank()

# importing SymPy libraries
from sympy.combinatorics.partitions import Partition
from sympy.combinatorics.partitions import RGS_unrank

# Using from sympy.combinatorics.partitions.Partition.RGS_unrank() method
rank = 10
n = 5
p = RGS_unrank(rank, n)

print ("unranked restricted growth string for super size 10 : \n", p)
