# import numpy
import numpy as np
import numpy.polynomial.laguerre as geek

ans = geek.lagvander2d((1, 2, 3, 4), (5, 6, 7, 8), [3, 3])

print(ans)
