# Convert 'Price' to numeric (float) type
combined_data['Price'] = pd.to_numeric(combined_data['Price'])
combined_data['Date'] = pd.to_datetime(combined_data['Date'])
combined_data.set_index('Date', inplace=True)

# Resample to weekly frequency
resampled_data = combined_data.groupby(['Ticker', pd.Grouper(freq='W')])['Price'].mean()
print(resampled_data)
