df['Value'] = df['Value'].where(df['Value'] != 0, df['Value'].shift())
print(df)
