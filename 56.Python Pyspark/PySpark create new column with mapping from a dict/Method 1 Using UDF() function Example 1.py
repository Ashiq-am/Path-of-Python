# PySpark create new column with
# mapping from a dict using UDF

# Import the libraries SparkSession, StringType and UDF
from pyspark.sql import SparkSession
from pyspark.sql.types import StringType
from pyspark.sql.functions import udf

# Create a spark session using getOrCreate() function
spark_session = SparkSession.builder.getOrCreate()

# Create a spark context
sc=spark_session.sparkContext

# Create a function to be called with mapping from a dict
def translate(dictionary):
	return udf(lambda col: dictionary.get(col),
			StringType())

# Create a data frame whose mapping has to be done
df = sc.parallelize([('B', ), ('D', ),
					('I', )]).toDF(['key'])

# Create a dictionary from where mapping needs to be done
dictionary = {'A': 'Apple', 'B': 'Ball',
			'C': 'Cat', 'D': 'Dog', 'E': 'Elephant'}

# Create a new column by calling the function to map the values
df.withColumn("value",
			translate(dictionary)("key")).show()
