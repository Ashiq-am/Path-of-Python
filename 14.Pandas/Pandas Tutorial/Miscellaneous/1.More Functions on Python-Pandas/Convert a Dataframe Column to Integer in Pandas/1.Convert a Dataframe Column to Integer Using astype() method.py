import pandas as pd

# Creating a sample DataFrame
data = {'Column1': ['1', '2', '3', '4']}
df = pd.DataFrame(data)

#Using astype() method
df['Column1'] = df['Column1'].astype(int)
print(df)
df['Column1'].dtype
