import pandas as pd

# Create a sample DataFrame
data = {
    'Region': ['North', 'North', 'North', 'South', 'South', 'South'],
    'Day': [1, 2, 3, 1, 2, 3],
    'Sales': [100, 200, 300, 400, 500, 600]
}

df = pd.DataFrame(data)

# Shift 'Sales' down by two rows within each group of 'Region'
df['Shifted_Sales_2'] = df.groupby('Region')['Sales'].shift(2)

# Display the DataFrame
print(df)
