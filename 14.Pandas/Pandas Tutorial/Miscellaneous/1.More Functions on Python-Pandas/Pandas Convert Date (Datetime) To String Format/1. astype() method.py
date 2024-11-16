# importing pandas as pd
import pandas as pd

# Create data with fields 'Date','Sales','Profit'
data = {
	'Date': pd.to_datetime(['2024-01-01', '2024-01-02', '2024-01-03']),
	'Sales': [101, 201, 301],
	'Profit': [909, 1809, 2709]
}
# Converting the data into dataframe by using pandas
df = pd.DataFrame(data)
print("Before conversion type:", type(df["Date"][0]))

# Using astype() method to convert 'Date' column values to Strings
df['Date'] = df['Date'].astype(str)
print("After conversion type:", type(df['Date'][0]))
