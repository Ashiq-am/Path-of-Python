import numpy as np

df_new = df.iloc[np.where(df.name.isin(li))]
