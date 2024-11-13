# import core() method from sympy
from sympy.ntheory.factor_ import core

n = 11 ** 4
k = 3

# Use core() method
core_n_k = core(n, k)

print("core({}, {}) = {} ".format(n, k, core_n_k))
