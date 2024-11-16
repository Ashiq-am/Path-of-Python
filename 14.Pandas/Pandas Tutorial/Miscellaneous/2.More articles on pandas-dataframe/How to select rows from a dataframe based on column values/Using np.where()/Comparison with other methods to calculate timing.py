# to calculate timing
import numpy as np
#% % timeit


# using mixture of numpy and pandas method
df_new = df.iloc[np.where(df.name.isin(li))]
