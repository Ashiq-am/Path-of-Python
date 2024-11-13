# Import necessary libraries
from pyspark.sql import SparkSession
from pyspark.sql.types import *

# Create a spark session
spark = SparkSession.builder.appName('Empty_Dataframe').getOrCreate()

# Create an expected schema
columns = StructType([StructField('Name',
								StringType(), True),
					StructField('Age',
								StringType(), True),
					StructField('Gender',
								StringType(), True)])

# Create a dataframe with expected schema
df = spark.createDataFrame(data = [],
						schema = columns)

# Print the datarame
print('Dataframe :')
df.show()

# Print the schema
print('Schema :')
df.printSchema()
