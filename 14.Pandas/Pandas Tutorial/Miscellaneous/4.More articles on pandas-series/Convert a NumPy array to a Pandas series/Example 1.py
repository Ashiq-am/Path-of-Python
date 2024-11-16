# importing the modules
import numpy as np
import pandas as pd

# creating an NumPy array
from IPython.core.display import display

array = np.array([10, 20, 1, 2,
				3, 4, 5, 6, 7])

# displaying the NumPy array
print("Numpy array is :")
display(array)

# converting the NumPy array
# to a Pandas series
series = pd.Series(array)

# displaying the Pandas series
print("Pandas Series : ")
display(series)
