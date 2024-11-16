# Calculating mean, median, and mode
mean_values = df.mean()
median_values = df.median()
mode_values = df.mode().iloc[0] # mode() returns a DataFrame

print("Mean values:\n", mean_values)
print("\nMedian values:\n", median_values)
print("\nMode values:\n", mode_values)
