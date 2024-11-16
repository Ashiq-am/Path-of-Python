# import numpy
import numpy as np
import numpy.polynomial.legendre as geek

ans = geek.legvander2d((1, 2, 3, 4), (5, 6, 7, 8), [3, 3])

print(ans)
