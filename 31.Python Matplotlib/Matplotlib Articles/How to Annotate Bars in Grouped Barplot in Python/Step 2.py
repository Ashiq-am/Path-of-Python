# transforming the dataset for barplot
data_df = df.groupby(['sex', 'class']).agg(
	avg_age=('age', 'mean'), count=('sex', 'count'))

data_df = data_df.reset_index()
print(data_df.head())
