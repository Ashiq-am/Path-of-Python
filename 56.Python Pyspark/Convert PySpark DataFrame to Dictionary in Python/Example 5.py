# Importing necessary libraries
from pyspark.sql import SparkSession

# Create a spark session
spark = SparkSession.builder.appName('DF_to_dict').getOrCreate()

# Create data in dataframe
data = [(('Hyderabad'), 120000),
		(('Delhi'), 124000),
		(('Mumbai'), 344000),
		(('Guntur'), 454000),
		(('Bandra'), 111200)]

# Column names in dataframe
columns = ["Location", 'House_price']

# Create the spark dataframe
df = spark.createDataFrame(data=data, schema=columns)

# Print the dataframe
print('Dataframe : ')
df.show()

# COnvert PySpark dataframe to
# pandas dataframe
df = df.toPandas()

# Convert the dataframe into
# dictionary
dict = df.to_dict(orient='list')

# Print the dictionary
print('Dictionary :')
print(dict)
