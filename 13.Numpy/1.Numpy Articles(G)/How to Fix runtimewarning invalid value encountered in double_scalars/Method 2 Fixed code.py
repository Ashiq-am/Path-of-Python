# Python program showing
# invalid error encounter in double scaler

import numpy as np
from scipy.special import logsumexp

x = 900
y = 711


# Solution of the error with the
# help of built-in function
sol1 = logsumexp(x) - logsumexp(y)

# sol1 = np.log(np.sum(np.exp(x)))/np.log(np.sum(np.exp(y)))
print("Now we can print our Answer :")
print(sol1)
