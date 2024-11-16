# import numpy library
import numpy as np

# create a numpy 1d-array
array1 = np.array([ 2, 4, 8])
array2 = np.array([ 3, 2,1])


# pearson product-moment correlation
# coefficients of the arrays
rslt2 = np.corrcoef(array1, array2)

print(rslt2)
