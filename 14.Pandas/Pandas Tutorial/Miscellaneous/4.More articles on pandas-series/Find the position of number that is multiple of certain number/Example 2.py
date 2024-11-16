# Importing Pandas and Numpy libraries
import pandas as pd
import numpy as np

# Creating a Series of random numbers
n_series = pd.Series(np.random.randint(1, 20, 10))
print("Original Series:\n")
print(n_series)

# Finding the indexes of numbers divisible by 3.5
res_index = np.argwhere(n_series % 3.5==0)
print("Positions of numbers that are multiples of 3.5:\n")
print(res_index)
