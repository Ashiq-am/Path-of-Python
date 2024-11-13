# PySpark create new column with
# mapping from a dict using map

# Import the libraries SparkSession, col, create_map, lit, chain
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, create_map, lit
from itertools import chain

# Create a spark session using getOrCreate() function
spark_session = SparkSession.builder.getOrCreate()

# Create a spark context
sc=spark_session.sparkContext

# Create a data frame whose mapping has to be done
df = sc.parallelize([('A', ), ('C', ),
					('G', )]).toDF(['key'])

# Create a dictionary from where mapping needs to be done
dictionary = {'A': 'Apple', 'B': 'Ball',
			'C': 'Cat', 'D': 'Dog',
			'E': 'Elephant'}

# Convert each item of dictionary to map type
mapping_expr = create_map([lit(x) for x in chain(*dictionary.items())])

# Create a new column by calling the function to map the values
df.withColumn("value",
			mapping_expr[col("key")]).show()
