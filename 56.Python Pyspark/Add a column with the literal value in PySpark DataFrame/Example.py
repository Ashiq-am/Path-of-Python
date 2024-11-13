# import SparkSession from the pyspark
from pyspark.sql import SparkSession

# bulid and create the
# SparkSession with name "lit_value"
spark = SparkSession.builder.appName("lit_value").getOrCreate()

# create the spark dataframe with columns A,B
data = spark.createDataFrame([('x',5),('Y',3),
							('Z',5) ],['A','B'])

# showing the schema and table
data.printSchema()
data.show()
