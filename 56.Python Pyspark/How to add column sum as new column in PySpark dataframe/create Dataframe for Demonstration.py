# import SparkSession from the pyspark
from pyspark.sql import SparkSession

# build and create the SparkSession
# with name "sum as new_col"
spark = SparkSession.builder.appName("sum as new_col").getOrCreate()

# Creating the Spark DataFrame
data = spark.createDataFrame([('x', 5, 3, 7),
							('Y', 3, 3, 6),
							('Z', 5, 2, 6)],
							['A', 'B', 'C', 'D'])

# Print the schema of the DataFrame by
# printSchema()
data.printSchema()

# Showing the DataFrame
data.show()
