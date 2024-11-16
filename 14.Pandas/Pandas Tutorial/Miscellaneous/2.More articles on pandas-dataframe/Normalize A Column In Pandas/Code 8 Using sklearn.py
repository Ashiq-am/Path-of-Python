from sklearn.preprocessing import MinMaxScaler
import numpy as np

# copy the data
df_sklearn = df.copy()

# apply normalization techniques
column = 'Column 1'
df_sklearn[column] = MinMaxScaler().fit_transform(np.array(df_sklearn[column]).reshape(-1,1))

# view normalized data
display(df_sklearn)
