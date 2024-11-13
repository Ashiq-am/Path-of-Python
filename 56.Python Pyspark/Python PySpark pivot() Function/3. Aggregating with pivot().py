# ...

# Sample data with multiple entries for the same product-region combination
data_with_duplicates = [
    ("A", "East", 100),
    ("A", "East", 50),
    ("A", "West", 150),
    ("B", "East", 200),
    ("B", "West", 250),
    ("B", "West", 100),
    ("C", "East", 300),
    ("C", "West", 350)
]

# Create a new DataFrame with duplicate data
df_with_duplicates = spark.createDataFrame(data_with_duplicates, columns)

# Pivot and sum the sales
pivot_df_with_aggregation_sum = df_with_duplicates.groupBy("Product").pivot("Region").sum("Sales")

# Show the result
pivot_df_with_aggregation_sum.show()

# Pivot and sum the sales
pivot_df_with_aggregation_avg = df_with_duplicates.groupBy("Product").pivot("Region").avg("Sales")

# Show the result
pivot_df_with_aggregation_avg.show()
