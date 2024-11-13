from pyspark.sql.functions import when

# ...

# Calculate total sales for products with sales greater than 1000
conditional_sum = sales_df.where("Sales > 1000").agg(sum("Sales").alias("Total_Sales_Above_1000"))
conditional_sum.show()
