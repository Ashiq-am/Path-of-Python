from pyspark.sql.functions import col

df.select(col("Name"),col("Marks")).show()
