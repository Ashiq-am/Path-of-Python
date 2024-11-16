# Sample DataFrame with a numerical column
data = {'Values': [5, 12, 18, 25, 32, 40, 50, 60]}
df = pd.DataFrame(data)
# Binning values into quantiles using pd.qcut
df['Quantile_Binned'] = pd.qcut(df['Values'], q=[0, 0.25, 0.5, 0.75, 1], labels=['Q1', 'Q2', 'Q3', 'Q4'])
# Print the DataFrame
print(df)
