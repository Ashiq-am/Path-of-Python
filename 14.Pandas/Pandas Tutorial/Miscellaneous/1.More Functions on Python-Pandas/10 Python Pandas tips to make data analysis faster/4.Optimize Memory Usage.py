# Optimize memory usage
df['column'] = df['column'].astype('float32')
# Updated DataFrame
print("\nDataFrame after optimizing memory usage:")
print(df)
print(df.info())
# Check memory usage after optimization
print("\nMemory usage after optimization:")
print(df.memory_usage())
