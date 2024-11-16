# Replace zeros with the previous non-zero value
df['Value'].replace(to_replace=0, method='ffill', inplace=True)

print(df)
