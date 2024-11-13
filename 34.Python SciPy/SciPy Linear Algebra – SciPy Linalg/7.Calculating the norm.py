# Importing the required libraries
from scipy import linalg
import numpy as np

# Initializing the input array
x = np.array([6 , 3])

# Calculating the L2 norm
a = linalg.norm(x)

# Calculating the L1 norm
b = linalg.norm(x , 1)

# Displaying the norm values
print(a)
print(b)
