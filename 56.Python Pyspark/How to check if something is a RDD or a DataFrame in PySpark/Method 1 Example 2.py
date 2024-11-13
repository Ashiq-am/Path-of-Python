# import DataFrame
from pyspark.sql import DataFrame

# import RDD
from pyspark.rdd import RDD

# need to import for session creation
from pyspark.sql import SparkSession

# creating the spark session
spark = SparkSession.builder.getOrCreate()

# create an rdd with some data
data = spark.sparkContext.parallelize([("1", "sravan", "vignan", 67, 89),
									("2", "ojaswi", "vvit", 78, 89),
									("3", "rohith", "vvit", 100, 80),
									("4", "sridevi", "vignan", 78, 80),
									("1", "sravan", "vignan", 89, 98),
									("5", "gnanesh", "iit", 94, 98)])

# check the data is rdd or not
print(isinstance(data, RDD))
