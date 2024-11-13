# Importing the required libraries
from scipy import linalg
import numpy as np

# Initializing the matrix
x = np.array([[16 , 4] , [100 , 25]])

# Calculate and print the matrix
# square root
r = linalg.sqrtm(x)
print(r)
print("\n")

# Calculate and print the matrix
# exponential
e = linalg.expm(x)
print(e)
print("\n")

# Calculate and print the matrix
# sine
s = linalg.sinm(x)
print(s)
print("\n")

# Calculate and print the matrix
# cosine
c = linalg.cosm(x)
print(c)
print("\n")

# Calculate and print the matrix
# tangent
t = linalg.tanm(x)
print(t)
