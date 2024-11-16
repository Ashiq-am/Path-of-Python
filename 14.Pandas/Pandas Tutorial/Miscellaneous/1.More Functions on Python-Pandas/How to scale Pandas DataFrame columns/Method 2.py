import seaborn as sns
from sklearn.preprocessing import MinMaxScaler
import pandas as pd

data = sns.load_dataset('iris')
print('Orginal Dataset')
data.head()

scaler = MinMaxScaler()

df_scaled = scaler.fit_transform(df.to_numpy())
df_scaled = pd.DataFrame(df_scaled, columns=[
'sepal_length', 'sepal_width', 'petal_length', 'petal_width'])

print("Scaled Dataset Using MinMaxScaler")
df_scaled.head()
