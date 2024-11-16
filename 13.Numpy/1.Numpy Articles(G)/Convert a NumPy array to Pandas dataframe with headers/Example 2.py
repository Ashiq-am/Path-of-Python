import numpy as np
import pandas as pd


arr = np.random.rand(6).reshape(2, 3)
print("Numpy array:")
print(arr)

# convert numpy array to dataframe
df = pd.DataFrame(arr, columns =['C1', 'C2', 'C3'])
print("\nPandas DataFrame: ")
df
