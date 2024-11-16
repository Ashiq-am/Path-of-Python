# Resample the DataFrame to weekly frequency
df_resampled = df.resample('W').agg({
  # Sum values in 'value1'
    'value1': 'sum',
   # Mean values in 'value2'
    'value2': 'mean',
  # Take the first value in 'value3'
    'value3': 'first'
})

print(df_resampled)
