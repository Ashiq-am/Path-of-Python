# Missing values in dataset..
columns = list(df)
for column in columns:
	print("No. of missing values in", column,
		"attribute:", df[column].isnull().sum())

# Dropping missing values
df = df.dropna(axis=0)
