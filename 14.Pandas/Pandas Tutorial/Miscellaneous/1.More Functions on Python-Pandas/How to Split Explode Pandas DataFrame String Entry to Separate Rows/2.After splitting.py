df[['Name1', 'Name2', 'Name3']] = df['Names'].str.split(',', expand=True)
print(df)
