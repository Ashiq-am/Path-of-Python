# Python code explaining
# SymPy.RGS_enum()

# importing SymPy libraries
from sympy.combinatorics.partitions import Partition
from sympy.combinatorics.partitions import RGS_enum

# Using from sympy.combinatorics.partitions.Partition.RGS_enum() method
p = RGS_enum(20)

q = RGS_enum(-1)

print ("no. of strings possible for size 20 ", p)
print ("no. of strings possible for size -1: ", q)
