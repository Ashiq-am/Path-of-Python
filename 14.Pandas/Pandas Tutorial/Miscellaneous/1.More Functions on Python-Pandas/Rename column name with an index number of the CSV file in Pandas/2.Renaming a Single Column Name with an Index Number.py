import pandas as pd
df = pd.read_csv('data.csv')
print(df.columns)
df = df.rename(columns={df.columns[1]: 'Years'})
df
