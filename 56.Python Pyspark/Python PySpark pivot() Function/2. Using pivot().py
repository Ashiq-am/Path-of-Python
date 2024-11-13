# ...

# Pivot the DataFrame
pivot_df = df.groupBy("Product").pivot("Region").sum("Sales")

# Show the pivoted DataFrame
pivot_df.show()
