# Apply the row_number function
df_row_number = df.withColumn("row_number", row_number().over(window_spec))

# Show all rankings
df_all_ranks = df_rank.join(df_dense_rank, ["customer_id", "trigger_id"]) \
                      .join(df_row_number, ["customer_id", "trigger_id"])
df_all_ranks.show()
