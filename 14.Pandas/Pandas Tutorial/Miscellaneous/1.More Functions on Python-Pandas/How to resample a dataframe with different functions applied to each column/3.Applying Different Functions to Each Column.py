# Define a dictionary of functions to apply to each column
agg_funcs = {
  # Max value in 'value1'
    'value1': 'max',
  # Median value in 'value2'
    'value2': lambda x: x.median(),
  # Most common value in 'value3'
    'value3': lambda x: x.mode().iloc[0]
}

# Resample the DataFrame with different functions
df_resampled_custom = df.resample('W').agg(agg_funcs)

print(df_resampled_custom)
