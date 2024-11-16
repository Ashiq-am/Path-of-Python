import numpy as geek
gfg = geek.array((0, 0, 0, 0, 1, 5, 7, 0, 6, 2, 9, 0, 10, 0, 0))

# without trim parameter
# returns an array without any trailing zeros

res = geek.trim_zeros(gfg, 'b')
print(res)
