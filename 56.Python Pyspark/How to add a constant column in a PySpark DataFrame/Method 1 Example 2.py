from pyspark.sql.functions import when, lit, col

df.withColumn(
"Great_Discount", when(col("Discount") >=1000,lit(
	"Yes")).otherwise(lit("NO"))).show()
