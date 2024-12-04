import pandas as pd
import numpy as np

df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})

# Replicate each row in df three times
df_replicated = pd.DataFrame(np.repeat(df.values, repeats=3, axis=0), columns=df.columns)
print(df_replicated)