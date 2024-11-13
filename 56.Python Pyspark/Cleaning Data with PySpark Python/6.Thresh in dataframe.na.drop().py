# Drop rows containing non-null values less than thresh
df_pyspark.na.drop(thresh=4).show()
