# Apply the dense_rank function
df_dense_rank = df.withColumn("dense_rank", dense_rank().over(window_spec))
df_dense_rank.show()
