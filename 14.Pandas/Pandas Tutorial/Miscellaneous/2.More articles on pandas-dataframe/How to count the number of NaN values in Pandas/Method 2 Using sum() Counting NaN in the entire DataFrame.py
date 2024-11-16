import pandas as pd
import numpy as np

# dictionary of lists
dict = {'A': [1, 4, 6, 9],
        'B': [np.NaN, 5, 8, np.NaN],
        'C': [7, 3, np.NaN, 2],
        'D': [1, np.NaN, np.NaN, np.NaN]}

# creating dataframe from the
# dictionary
data = pd.DataFrame(dict)

# total count of NaN values
print(data.isnull().sum().sum())
