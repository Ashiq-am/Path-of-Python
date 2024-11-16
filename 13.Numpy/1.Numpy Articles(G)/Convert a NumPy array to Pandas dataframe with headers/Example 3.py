import numpy as np
import pandas as pd


arr = np.array([[1, 2], [4, 5]])
print("Numpy array:")
print(arr)

# convert numpy array to dataframe
df = pd.DataFrame(data = arr, index =["row1", "row2"],
				columns =["col1", "col2"])

print("\nPandas DataFrame: ")
df
