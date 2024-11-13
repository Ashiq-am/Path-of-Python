# import DataFrame
from pyspark.sql import DataFrame

# import RDD
from pyspark.rdd import RDD

# need to import for session creation
from pyspark.sql import SparkSession

# creating the spark session
spark = SparkSession.builder.getOrCreate()

# create an rdd with some data
rdd = spark.sparkContext.parallelize([(1, "Sravan", "vignan", 98),
									(2, "bobby", "bsc", 87)])

# check if it is an RDD
print(" RDD : ", isinstance(rdd, RDD))

# check if it is an DataFrame
print("Dataframe : ", isinstance(rdd, DataFrame))

# display data of rdd
print("Rdd Data : \n", rdd.collect())

# convert rdd to dataframe
data = rdd.toDF()

# check if it is an RDD
print("RDD : ", isinstance(rdd, RDD))

# check if it is an DataFrame
print("Dataframe : ", isinstance(rdd, DataFrame))

# display dataframe
data.collect()
