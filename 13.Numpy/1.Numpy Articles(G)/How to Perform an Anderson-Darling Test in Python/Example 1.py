# Python program to conduct Anderson-Darling Test

# Importing libraries
import numpy as np
from scipy.stats import anderson

# Creating data
np.random.seed(0)
data = np.random.normal(size=100)

# Conduct Anderson-Darling Test
anderson(data)
