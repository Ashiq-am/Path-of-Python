# import core() method from sympy
from sympy.ntheory.factor_ import core

n = 24
k = 2

# Use core() method
core_n_k = core(n, k)

print("core({}, {}) = {} ".format(n, k, core_n_k))
