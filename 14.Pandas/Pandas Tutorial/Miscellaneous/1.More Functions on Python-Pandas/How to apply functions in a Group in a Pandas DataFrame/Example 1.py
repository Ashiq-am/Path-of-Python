# finding rolling mean
rolling_mean = data_df.groupby("Student House")["Points"].apply(
	lambda x: x.rolling(center=False, window=2).mean())

print("Rolling Mean:")
print(rolling_mean)
