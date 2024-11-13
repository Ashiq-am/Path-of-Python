from pyspark.sql import SparkSession

spark = SparkSession.builder.appName(
	"HiveQuery").enableHiveSupport().getOrCreate()

result = spark.sql("SELECT name FROM customers WHERE state='CA' AND city='LA'")
result.show()
