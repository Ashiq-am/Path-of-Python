# using groupby function with aggregation
# to get mean, min and max values
result = df.groupby('Team').agg({'Age': ['mean', 'min', 'max']})

print("Mean, min, and max values of Age grouped by Team")
print(result)
