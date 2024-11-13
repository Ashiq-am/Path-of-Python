# PySpark create new columns with
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
df = sc.parallelize([(1, ), (2, ),
					(3, )]).toDF(['Roll_Number'])

# Create a dictionary from where mapping needs to be done
dictionary={'names': {1: 'Vinayak',
					2: 'Ishita',
					3: 'Arun'},
			'subject': {1: 'Maths',
						2: 'Chemistry',
						3:'English'},
			'fees':{1:10000, 2: 13000, 3: 15000}}

# Create a new column 'Name' by calling the function to map the values
df=df.withColumn("Name",
				translate(dictionary['names'])("Roll_Number"))

# Create a new column 'Subject' by calling the function to map the values
df=df.withColumn("Subject",
				translate(dictionary['subject'])("Roll_Number"))

# Create a new column 'Fees' by calling the function to map the values
df=df.withColumn("Fees",
				translate(dictionary['fees'])("Roll_Number"))

# Display the data frame
df.show()
