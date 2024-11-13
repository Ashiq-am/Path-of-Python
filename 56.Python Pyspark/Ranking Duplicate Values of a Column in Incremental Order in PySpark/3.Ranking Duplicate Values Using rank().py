# Define the window specification
window_spec = Window.partitionBy("trigger_id").orderBy("customer_id")

# Apply the rank function
df_rank = df.withColumn("rank", rank().over(window_spec))
df_rank.show()
