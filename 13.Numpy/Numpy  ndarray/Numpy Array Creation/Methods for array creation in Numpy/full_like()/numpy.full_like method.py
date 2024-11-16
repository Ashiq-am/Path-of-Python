# Python Programming illustrating
# numpy.full_like method

import numpy as geek

x = geek.arange(10, dtype = int).reshape(2, 5)
print("x before full_like : \n", x)

# using full_like
print("\nx after full_like : \n", geek.full_like(x, 10.0))

y = geek.arange(10, dtype = float).reshape(2, 5)
print("\n\ny before full_like : \n", x)

# using full_like
print("\ny after full_like : \n", geek.full_like(y, 0.01))
