# importing packages
import pandas.api.types as pd
import numpy as np

datetime_array = np.array([], dtype=np.datetime64)
print(pd.is_datetime64_dtype(datetime_array))
