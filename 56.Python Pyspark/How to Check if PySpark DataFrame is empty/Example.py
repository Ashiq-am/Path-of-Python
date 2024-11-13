# import modules
from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType

# defining schema
schema = StructType([
	StructField('COUNTRY', StringType(), True),
	StructField('CITY', StringType(), True),
	StructField('CAPITAL', StringType(), True)
])

# Create Spark Object
spark = SparkSession.builder.appName("TestApp").getOrCreate()

# Create Empty DataFrame with Schema.
df = spark.createDataFrame([], schema)

# Show schema and data
df.printSchema()
df.show(truncate=False)
