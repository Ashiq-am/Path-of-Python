import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(10000, 4))
df.iloc[:9998] = np.nan

sdf = df.astype(pd.SparseDtype("float", np.nan))

sdf.head()

sdf.dtypes
