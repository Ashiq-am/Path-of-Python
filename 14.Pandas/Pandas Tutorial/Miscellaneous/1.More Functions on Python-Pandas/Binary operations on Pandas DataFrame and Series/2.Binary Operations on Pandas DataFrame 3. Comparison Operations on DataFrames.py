import pandas as pd
df1 = pd.DataFrame({'A': [10, 20, 30], 'B': [40, 50, 60]})
df2 = pd.DataFrame({'A': [5, 15, 35], 'B': [30, 60, 55]})

# Checking if elements of df1 are greater than df2
result = df1 > df2
print(result)