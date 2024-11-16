# importing the modules
import numpy as np
import pandas as pd

# creating an NumPy array
from IPython.core.display import display

array = np.random.rand(5)

# displaying the NumPy array
print("Numpy array is :")
display(array)

# converting the NumPy array
# to a Pandas series
series = pd.Series(array)

# displaying the Pandas series
print("Pandas Series : ")
display(series)
