import numpy as np
import pandas as pd


arr = np.random.rand(4, 3)
print("Numpy array:")
print(arr)

# convert numpy array to dataframe
df = pd.DataFrame(arr, columns =['A', 'B', 'C'])
print("\nPandas DataFrame: ")
df
