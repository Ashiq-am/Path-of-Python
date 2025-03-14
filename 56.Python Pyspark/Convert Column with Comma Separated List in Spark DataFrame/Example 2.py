from pyspark.sql import SparkSession
from pyspark.sql.functions import split, col, explode

# create sample data
data = [("1", "java,swift"), ("2", "python, ruby"), ("3", "java,python")]
columns = ["user_id", "items"]

# create Spark session and DataFrame
spark = SparkSession.builder.appName(
	"Comma Separated List Example").getOrCreate()
df = spark.createDataFrame(data, columns)

# extract list items into an array
df = df.withColumn("item_list", split(col("items"), ","))

# show list
df.show()

# stop SparkSession
spark.stop()
