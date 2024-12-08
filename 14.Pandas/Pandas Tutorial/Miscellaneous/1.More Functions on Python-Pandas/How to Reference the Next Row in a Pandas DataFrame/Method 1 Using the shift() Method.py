import pandas as pd

data = {'X': [10, 20, 30], 'Y': [5, 15, 25]}
df = pd.DataFrame(data)

# Create a new column referencing the next row
df['X_next'] = df['X'].shift(-1)
print(df)