# finding sum
sum = data_df.groupby("Student House")["Points"].apply(
lambda x: x.sum())

print("Sum:")
print(sum)
