# Splitting the 'Name' column by the letter 'l' and taking the first part
df['Name_Split'] = df['Name'].str.split('l').str[0]
print(df)
