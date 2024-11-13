# Python3 code to demonstrate working of
# N element incremental tuples
# Using generator expression + tuple
from itertools import repeat

# initialize N
N = 3

# printing N
print("Number of times to repeat : " + str(N))

# N element incremental tuples
# Using generator expression + tuple
res = tuple(tuple(repeat(ele, N)) for ele in range(1, 6))

# printing result
print("Tuple sequence : " + str(res))
