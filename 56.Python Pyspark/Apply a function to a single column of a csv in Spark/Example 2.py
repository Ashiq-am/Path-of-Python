from pyspark.sql.functions import col

# Incrementing the value of each column by 1
df = df.withColumn("age", col("age") + 1)

df.show()
