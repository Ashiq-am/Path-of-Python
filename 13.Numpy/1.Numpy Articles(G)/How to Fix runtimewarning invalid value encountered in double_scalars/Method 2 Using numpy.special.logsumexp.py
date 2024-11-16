import numpy as np
from numpy import sinh

x = 900
y = 711

# This operation raise error
sol1 = np.log(np.sum(np.exp(x)))/np.log(np.sum(np.exp(y)))

print(sol1)
