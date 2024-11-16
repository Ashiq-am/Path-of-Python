# import numpy
import numpy as np
import numpy.polynomial.polynomial as geek

ans = geek.polyvander3d((1, 2), (3, 4), (5, 6), [3, 3, 3])

print(ans)
