df['Value'] = df['Value'].replace(0, pd.NA).ffill()
print(df)
