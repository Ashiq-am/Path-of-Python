# import numpy
import numpy as np
import numpy.polynomial.legendre as geek

ans = geek.legvander((1, 2, 3, 4), 3)

print(ans)
