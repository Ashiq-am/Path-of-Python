# Convert UTC timestamps to local time zone
local_timezone = pytz.timezone('America/New_York') # Example: Convert to New York time zone

df['timestamp_local'] = df['timestamp_utc'].dt.tz_localize('UTC').dt.tz_convert(local_timezone)

# Display the DataFrame with local time zone
print("\nDataFrame with local time zone:")
print(df)
