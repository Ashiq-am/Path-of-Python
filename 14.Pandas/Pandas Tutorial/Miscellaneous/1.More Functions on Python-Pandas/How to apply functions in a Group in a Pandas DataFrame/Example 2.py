# finding mean
mean = data_df.groupby("Student House")["Points"].apply(
lambda x: x.mean())

print("Mean:")
print(mean)
