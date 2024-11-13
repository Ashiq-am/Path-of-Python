# Python code explaining
# SymPy.RGS_enum()

# importing SymPy libraries
from sympy.combinatorics.partitions import Partition
from sympy.combinatorics.partitions import RGS_enum

# Using from sympy.combinatorics.partitions.Partition.RGS_enum() method
p = RGS_enum(4)

q = RGS_enum(9)

print ("no. of strings possible for size 4: ", p)
print ("no. of strings possible for size 9: ", q)
