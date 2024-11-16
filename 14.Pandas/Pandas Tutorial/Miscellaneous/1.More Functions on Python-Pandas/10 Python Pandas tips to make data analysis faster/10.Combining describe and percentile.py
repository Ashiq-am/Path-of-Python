import pandas as pd
# Sample DataFrame
data = {'Value': [10, 15, 20, 25, 30, 35, 40, 45, 50]}
df = pd.DataFrame(data)
# Using describe to get summary statistics including specific percentiles
summary_stats = df['Value'].describe(percentiles=[0.25, 0.5, 0.75])
print(summary_stats)
