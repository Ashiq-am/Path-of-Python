# Import necessary libraries
from pyspark.sql import SparkSession
from pyspark.sql.types import *

# Create a spark session
spark = SparkSession.builder.appName('Empty_Dataframe').getOrCreate()

# Create an empty RDD
emp_RDD = spark.sparkContext.emptyRDD()

# Create an expected schema
columns = StructType([StructField('Name',
								StringType(), True),
					StructField('Age',
								StringType(), True),
					StructField('Gender',
								StringType(), True)])

# Create an empty RDD with expected schema
df = spark.createDataFrame(data = emp_RDD,
						schema = columns)

# Print the datarame
print('Dataframe :')
df.show()

# Print the schema
print('Schema :')
df.printSchema()
