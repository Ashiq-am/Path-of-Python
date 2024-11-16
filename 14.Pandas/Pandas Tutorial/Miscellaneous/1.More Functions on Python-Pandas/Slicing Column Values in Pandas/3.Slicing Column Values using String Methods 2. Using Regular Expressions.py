# Extracting only the digits from the 'City' column (although in this case, there are none)
df['City_Digits'] = df['City'].str.extract('(\d+)', expand=False)
print(df)
