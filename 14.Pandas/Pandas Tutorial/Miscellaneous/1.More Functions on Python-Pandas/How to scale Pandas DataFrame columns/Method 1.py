import seaborn as sns
import pandas as pd
import numpy as np

data = sns.load_dataset('iris')
print('Orginal Dataset')
data.head()

# Min-Max Normalization
df = data.drop('species', axis=1)
df_norm = (df-df.min())/(df.max()-df.min())
df_norm = pd.concat((df_norm, data.species), 1)

print("Scaled Dataset Using Pandas")
df_norm.head()
