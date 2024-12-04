import numpy as np
import pandas as pd
# Two-dimensional array
array_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
df_2d = pd.DataFrame(array_2d, columns=['A', 'B', 'C'])
print(df_2d)