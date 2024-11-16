import pandas as pd

# Create a sample DataFrame
data = {
    'Region': ['North', 'North', 'North', 'South', 'South', 'South'],
    'Day': [1, 2, 3, 1, 2, 3],
    'Sales': [100, 200, 300, 400, 500, 600]
}

df = pd.DataFrame(data)

# Shift 'Sales' down by one row within each group and fill missing values with 0
df['Shifted_Sales_2'] = df.groupby('Region')['Sales'].shift(1, fill_value=0)

# Display the DataFrame
print(df)
