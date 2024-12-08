import pandas as pd

df = pd.DataFrame({'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
                   'Sales': [200, 220, 250, 300, 280, 310]})
df['Shifted_Sales'] = df['Sales'].shift(-4)
print(df)

df['Shifted_Sales'] = df['Sales'].shift(2)
print(df)