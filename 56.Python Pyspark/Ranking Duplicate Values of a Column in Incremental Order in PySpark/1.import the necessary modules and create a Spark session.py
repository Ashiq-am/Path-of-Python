from pyspark.sql import SparkSession
from pyspark.sql.window import Window
from pyspark.sql.functions import rank, dense_rank, row_number

# Create a Spark session
spark = SparkSession.builder.appName("RankDuplicates").getOrCreate()
