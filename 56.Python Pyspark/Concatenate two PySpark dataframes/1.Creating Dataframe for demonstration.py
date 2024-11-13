# Importing necessary libraries
from pyspark.sql import SparkSession

# Create a spark session
spark = SparkSession.builder.appName('pyspark - example join').getOrCreate()

# Create data in dataframe
data = [(('Ram'), '1991-04-01', 'M', 3000),
		(('Mike'), '2000-05-19', 'M', 4000),
		(('Rohini'), '1978-09-05', 'M', 4000),
		(('Maria'), '1967-12-01', 'F', 4000),
		(('Jenis'), '1980-02-17', 'F', 1200)]

# Column names in dataframe
columns = ["Name", "DOB", "Gender", "salary"]

# Create the spark dataframe
df1 = spark.createDataFrame(data=data, schema=columns)

# Print the dataframe
df1.show()
