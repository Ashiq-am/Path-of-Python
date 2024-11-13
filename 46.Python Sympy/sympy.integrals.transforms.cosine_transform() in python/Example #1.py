# import cosine_transform
from sympy import cosine_transform, exp, sqrt, cos
from sympy.abc import x, k, a

# Using cosine_transform() method
gfg = cosine_transform(exp(-a * x), x, k)

print(gfg)
