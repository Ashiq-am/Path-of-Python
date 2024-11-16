# importing packages
import numpy as np

# setting seed
np.random.seed(101)

# creating random arrays
a = np.random.rand(2, 2)
print(a)
b = np.random.rand(2, 3)
print(b)
c = np.random.rand(3, 2)
print(c)

# lowest cost contraction order for an einsum expression
path = np.einsum_path('ij,jk,kl->il', a, b, c, optimize='greedy')

# Path info
print(path[0])
print(path[1])
