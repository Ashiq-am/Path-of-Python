import pandas as pd

# Create a sample DataFrame
data = {
    'Region': ['North', 'North', 'North', 'South', 'South', 'South'],
    'Day': [1, 2, 3, 1, 2, 3],
    'Sales': [100, 200, 300, 400, 500, 600]
}

df = pd.DataFrame(data)

# Shift both 'Sales' and 'Day' down by one row within each 'Region' group
df[['Shifted_Sales', 'Shifted_Day']] = df.groupby('Region')[['Sales', 'Day']].shift(1)

# Display the DataFrame
print(df)
