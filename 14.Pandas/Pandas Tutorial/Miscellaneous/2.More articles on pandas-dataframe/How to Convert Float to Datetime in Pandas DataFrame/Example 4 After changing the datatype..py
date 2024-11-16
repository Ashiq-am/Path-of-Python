# converting the float to datetime format
# in multiple columns
df['Starting_Date'] = pd.to_datetime(df['Starting_Date'],
									format='%Y%m%d')
df['Ending_Date'] = pd.to_datetime(df['Ending_Date'],
								format='%Y%m%d')

# printing dataframe
print(df)
print()

print(df.dtypes)
