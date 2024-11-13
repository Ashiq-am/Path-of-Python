# finding Skewness

from scipy.stats import skew
import numpy as np

# random values based on a normal distribution
x = np.random.normal(0, 2, 10000)

print ("X : \n", x)

print('\nSkewness for data : ', skew(x))
