# Import required libraries
import numpy as np
from numpy.polynomial import hermite_e

# Now define a polynomial you want to convert
pol = np.array([4, 2, 3, 6])

# Now convert the polynomial to
# a Hermite Series (Probabilist's Hermite Series)
converted = hermite_e.poly2herme(pol)

# Now print the results
print("Coefficients of the defined polynomial:", pol)
print("Converting by Probabilist's Hermite series..")
print("Coefficients of the converted \
equivalent Hermite series :", converted)
