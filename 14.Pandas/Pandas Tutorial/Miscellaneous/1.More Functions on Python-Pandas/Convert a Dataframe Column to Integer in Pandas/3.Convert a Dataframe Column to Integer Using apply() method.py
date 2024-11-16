import pandas as pd

# Creating a sample DataFrame
data = {'Column1': ['1', '2', '3', '4']}
df = pd.DataFrame(data)

# Using apply() method with a lambda function
df = pd.DataFrame(data)
df['Column1'] = df['Column1'].apply(lambda x: int(x))
print(df)
df['Column1'].dtype
