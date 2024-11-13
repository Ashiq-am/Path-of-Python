# If you want to convert data to numeric
# types you can cast as follows
import findspark
findspark.init('c:/spark')

# import required modules
from pyspark.sql import SparkSession
from pyspark.sql.functions import split, col
from pyspark.sql.types import ArrayType, IntegerType

def return_array(column):
		return split(col(column),",")

# start the spark session
spark = SparkSession.builder \
		.appName('GeeksforGeeks') \
		.getOrCreate()

# create the dataframe
data = [("Pulkit, Dhingra","M","70,85"),
			("Ritika, Pandey","F","85,95"),
			("Kaif, Ali","M","63,72"),
			("Asha, Deep","F","62,92")
			]

columns=["Name","Gender","Marks"]
df=spark.createDataFrame(data,columns)
df.show()

# use split function
df2 = df.select(split(col("Name"),",").alias("Name"),
	split(col("Gender"),",").alias("Gender"),
	split(col("Marks"),",").alias("Marks_Arr"))
df2.show()

# stop session
spark.stop()
