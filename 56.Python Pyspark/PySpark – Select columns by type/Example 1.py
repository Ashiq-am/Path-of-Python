# importing module
import pyspark

# importing sparksession from pyspark.sql module
from pyspark.sql import SparkSession

# import data field types
from pyspark.sql.types import (StringType,
DoubleType, IntegerType, StructType,
StructField, FloatType)


# creating sparksession and giving an app name
spark = SparkSession.builder.appName('sparkdf').getOrCreate()

# list of student data
data = [(1, "sravan", 9.8, 4500.00), (2, "ojsawi",
									9.2, 6789.00),
		(3, "bobby", 8.9, 988.000)]

# specify column names with data types
columns = StructType([
	StructField("ID", IntegerType(), True),
	StructField("NAME", StringType(), True),
	StructField("GPA", FloatType(), True),
	StructField("FEE", DoubleType(), True),

])

# creating a dataframe from the lists of data
dataframe = spark.createDataFrame(data, columns)

# select columns that are integer type
print(dataframe[[item[0]
				for item in dataframe.dtypes if item[
				1].startswith('int')]].collect())

# select columns that are string type
print(dataframe[[item[0]
				for item in dataframe.dtypes if item[
				1].startswith('string')]].collect())

# select columns that are float type
print(dataframe[[item[0]
				for item in dataframe.dtypes if item[
				1].startswith('float')]].collect())

# select columns that are double type
print(dataframe[[item[0]
				for item in dataframe.dtypes if item[
				1].startswith('double')]].collect())
