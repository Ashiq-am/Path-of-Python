# converting the string to datetime format
df['Dates'] = pd.to_datetime(df['Dates'], format='%y%m%d')

# printing dataframe
print(df)
print()

print(df.dtypes)
