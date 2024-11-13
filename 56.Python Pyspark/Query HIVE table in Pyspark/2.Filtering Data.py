from pyspark.sql import SparkSession

spark = SparkSession.builder.appName(
	"HiveQuery").enableHiveSupport().getOrCreate()

result = spark.sql("SELECT name, age FROM employees WHERE age > 35")
result.show()
