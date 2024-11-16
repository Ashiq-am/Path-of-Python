# Create a sample DataFrame with datetime columns
data = {
	'timestamp_utc': [
		'2024-02-07 08:00:00',
		'2024-02-07 12:00:00',
		'2024-02-07 16:00:00'
	]
}
df = pd.DataFrame(data)
df['timestamp_utc'] = pd.to_datetime(df['timestamp_utc'])

# Display the DataFrame
print("DataFrame with UTC timestamps:")
print(df)
