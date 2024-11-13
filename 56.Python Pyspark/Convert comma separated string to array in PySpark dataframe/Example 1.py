# import required modules
from pyspark.sql import SparkSession
from pyspark.sql.functions import split, col

# start the spark session
spark = SparkSession.builder \
		.appName('GeeksforGeeks') \
		.getOrCreate()

# create the dataframe
data = [("Pulkit, Dhingra","M",70),
			("Ritika, Pandey","F",85),
			("Kaif, Ali","M",63),
			("Asha, Deep","F",62)
			]

columns=["Name","Gender","Marks"]
df=spark.createDataFrame(data,columns)

# use split function
df2 = df.select(split(col("Name"),",").alias("Name_Arr"),
				col("Gender"),col("Marks")) \
	.drop("Name")

df2.show()

# stop session
spark.stop()
