# Import necessary libraries
from pyspark.sql import SparkSession
from pyspark.sql.types import *

# Create a spark session
spark = SparkSession.builder.appName('Empty_Dataframe').getOrCreate()

# Create an empty schema
columns = StructType([])

# Create an empty dataframe with empty schema
df = spark.createDataFrame(data = [],
						schema = columns)

# Print the datarame
print('Dataframe :')
df.show()

# Print the schema
print('Schema :')
df.printSchema()
