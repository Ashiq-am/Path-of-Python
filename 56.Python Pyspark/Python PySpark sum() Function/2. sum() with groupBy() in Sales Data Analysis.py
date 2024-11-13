# Sample sales data
sales_data = [
    ("Laptop", 1200.00),
    ("Smartphone", 800.00),
    ("Tablet", 600.00),
    ("Laptop", 1500.00),
    ("Smartphone", 950.00)
]

# Create DataFrame
sales_df = spark.createDataFrame(sales_data, ["Product", "Sales"])

# Show the DataFrame
sales_df.show()

# Calculate total sales for each product
total_sales_by_product = sales_df.groupBy("Product").agg(sum("Sales").alias("Total_Sales"))
total_sales_by_product.show()
