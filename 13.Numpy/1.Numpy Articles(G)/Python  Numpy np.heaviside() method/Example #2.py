# import numpy
import numpy as np

x = np.zeros(5)
y = np.array([-1.5, 0.5, 0, 0.5, -1.5])

# using np.heaviside() method
gfg = np.heaviside(x, y)

print(gfg)
