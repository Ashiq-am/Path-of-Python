# Categorize the 'Values' column into 4 quantiles
df['Quantile Categories'] = pd.qcut(df['Values'], 4)

print(df)
