# Calculate daily returns
df['Return'] = df.Close.pct_change()
