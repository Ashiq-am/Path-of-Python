from pyspark.sql import SparkSession
from pyspark.sql.functions import split, explode, col

from pyspark.sql.functions import collect_list, concat_ws

# create sample data
data = [("1", ["user1"], "Admin"),
		("2", ["user1"], "Accounts"),
		("3", ["user2"], "finance"),
		("4", ["user3"], "sales"),
		("5", ["user3"], "finance")]
columns = ["ID", "USER_LIST", "DEPT_LIST"]

# create Spark session and DataFrame
spark = SparkSession.builder.appName(
	"Comma Separated List Example").getOrCreate()
df = spark.createDataFrame(data, columns)

# explode the USER_LIST column
df = df.select("ID", explode("USER_LIST").alias("USER"), "DEPT_LIST")

# group the dataframe by USER and concatenate the DEPT_LIST
df = df.groupBy("USER").agg(min("ID").alias("ID"),
							collect_list("DEPT_LIST").alias("DEPT_LIST"))
df = df.withColumn("DEPT_LIST", concat_ws(",", col("DEPT_LIST")))
# show the output table
df.show()

# stop SparkSession
spark.stop()
