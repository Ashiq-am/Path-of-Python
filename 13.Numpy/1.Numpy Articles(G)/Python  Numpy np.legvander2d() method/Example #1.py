# import numpy
import numpy as np
import numpy.polynomial.legendre as geek

# using np.legvander() method
ans = geek.legvander2d((1, 3, 5, 7), (2, 4, 6, 8), [2, 2])

print(ans)
