# converting the float to datetime format
df['Dates'] = pd.to_datetime(df['Dates'], format='%Y%m%d')

# printing dataframe
print(df)
print()

print(df.dtypes)
