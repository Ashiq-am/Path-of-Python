# Importing required modules
from pyspark.sql.functions import udf
from pyspark.sql.types import StringType
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("gfg").getOrCreate()

# Define the Python function
def concat_strings(x, y):
	return x + ' ' + y

# Create the UDF
concat_strings_udf = udf(concat_strings,
						StringType())

# Create data frame
df = spark.createDataFrame([('John', 'Doe'),
							('Adam', 'Smith'),
							('Jane','Doe')],
						['first_name',
							'last_name'])
df.show()

print("after applying udf function")
df.select(concat_strings_udf(
'first_name','last_name').alias(
'full_name')).show()
