# Import required modules
from pyspark.sql.functions import udf
from pyspark.sql.types import IntegerType
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("gfg").getOrCreate()

# Define the Python function
def square(x):
	return x * x

# Create the UDF
square_udf = udf(square,
				IntegerType())

# Use the UDF in a DataFrame operation
df = spark.range(1, 10)
df.select(square_udf("id").alias(
"squared")).show()
