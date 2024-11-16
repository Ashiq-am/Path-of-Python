# Extracting the first three characters of each name
df['Name_Short'] = df['Name'].str[:3]
print(df)
