import pandas as pd
import numpy as np

# importing our dataset
data = pd.read_csv('cluster_blobs.csv')

# viewing the dataFrame
print(data)

# we convert the datatype of
# columns from float to int.
data = data.apply(np.int64)

# viewing the modified column
print(data)
