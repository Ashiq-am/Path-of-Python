# Localize UTC timestamps to UTC time zone
df['timestamp_local'] = df['timestamp_utc'].dt.tz_localize('UTC')

# Convert localized timestamps to local time zone (Asia/Kolkata)
df['timestamp_local'] = df['timestamp_local'].dt.tz_convert('Asia/Kolkata')

# Display the DataFrame with local time zone
print("\nDataFrame with local time zone (Asia/Kolkata):")
print(df)
