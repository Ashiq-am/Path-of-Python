# need to import for session creation
from pyspark.sql import SparkSession

# creating the spark session
spark = SparkSession.builder.getOrCreate()

# create an rdd with some data
rdd = spark.sparkContext.parallelize([(1, "Sravan","vignan",98),
									(2, "bobby","bsc",87)])

# check the type using type() command
print(type(rdd))
