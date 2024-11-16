# Import pandas library
import pandas as pd

# Creating a DataFrame
df = pd.DataFrame({
	'Age': [28, 35, 42, 99, 87],
	'Name': ['Allen', 'Ravindra', 'Henry', 'Keshav', 'Shami']
})

# Extracting the 'Age' column
age_series = df['Age']

# Renaming the Series
renamed_series = age_series.rename("Ages")

# Print the renamed series
print(renamed_series)
