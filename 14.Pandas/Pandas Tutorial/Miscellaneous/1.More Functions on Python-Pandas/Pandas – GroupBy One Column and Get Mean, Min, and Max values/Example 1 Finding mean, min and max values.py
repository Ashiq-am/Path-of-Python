# using groupby function with aggregation
# to get mean, min and max values
result = df.groupby('Type').agg({'top_speed(mph)': ['mean', 'min', 'max']})

print("Mean, min, and max values of Top Speed grouped by Vehicle Type")
print(result)
