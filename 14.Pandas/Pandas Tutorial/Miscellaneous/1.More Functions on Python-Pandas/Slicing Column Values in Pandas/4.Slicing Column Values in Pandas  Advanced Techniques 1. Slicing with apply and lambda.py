# Extracting the first letter of each city name
df['City_First_Letter'] = df['City'].apply(lambda x: x[0])
print(df)
