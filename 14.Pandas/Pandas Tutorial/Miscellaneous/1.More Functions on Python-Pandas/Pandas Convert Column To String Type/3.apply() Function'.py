import pandas as pd

# sample data
data = {'NumericColumn': [1, 2, 3, 4]}
df = pd.DataFrame(data)
df['NumericColumn'] = df['NumericColumn'].apply(lambda x: str(x))
df.info()
