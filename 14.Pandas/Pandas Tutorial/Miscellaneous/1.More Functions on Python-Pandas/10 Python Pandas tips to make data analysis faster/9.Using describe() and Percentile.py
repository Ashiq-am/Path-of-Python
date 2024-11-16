import pandas as pd
# Sample DataFrame
data = {'Value': [10, 15, 20, 25, 30, 35, 40, 45, 50]}
df = pd.DataFrame(data)
# Using describe to get summary statistics
summary_stats = df['Value'].describe()
print(summary_stats)
# Calculate specific percentiles
percentile_25 = df['Value'].quantile(0.25)
percentile_50 = df['Value'].quantile(0.50) # Median
percentile_75 = df['Value'].quantile(0.75)
print(f'25th Percentile: {percentile_25}')
print(f'50th Percentile (Median): {percentile_50}')
print(f'75th Percentile: {percentile_75}')
