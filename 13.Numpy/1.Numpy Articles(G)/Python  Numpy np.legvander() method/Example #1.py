# import numpy
import numpy as np
import numpy.polynomial.legendre as geek

# using np.legvander() method
ans = geek.legvander((1, 3, 5, 7), 2)

print(ans)
