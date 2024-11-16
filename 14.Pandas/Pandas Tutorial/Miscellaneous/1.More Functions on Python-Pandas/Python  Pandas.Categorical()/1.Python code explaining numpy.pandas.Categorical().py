# Python code explaining
# numpy.pandas.Categorical()

# importing libraries
import numpy as np
import pandas as pd

# Categorical using dtype
c = pd.Series(["a", "b", "d", "a", "d"], dtype ="category")
print ("\nCategorical without pandas.Categorical() : \n", c)


c1 = pd.Categorical([1, 2, 3, 1, 2, 3])
print ("\n\nc1 : ", c1)

c2 = pd.Categorical(['e', 'm', 'f', 'i',
					'f', 'e', 'h', 'm' ])
print ("\nc2 : ", c2)
