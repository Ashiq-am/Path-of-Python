# converting the string to datetime
# format in multiple columns
df['Treatment_start'] = pd.to_datetime(
						df['Treatment_start'],
						format='%Y%m%d'
)
df['Treatment_end'] = pd.to_datetime(
						df['Treatment_end'],
						format='%Y%m%d'
)


# printing dataframe
print(df)
print()

print(df.dtypes)
