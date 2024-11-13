from pyspark.sql import SparkSession

spark = SparkSession.builder.appName(
	"HiveQuery").enableHiveSupport().getOrCreate()

result = spark.sql(
	"SELECT state, SUM(amount) as total_sales FROM sales GROUP BY state")
result.show()
