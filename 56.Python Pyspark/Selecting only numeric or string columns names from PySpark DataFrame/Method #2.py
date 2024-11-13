from pyspark.sql.types import StringType, LongType
from pyspark.sql import Row
from datetime import date
from pyspark.sql import SparkSession


# Initializing spark session
spark = SparkSession.builder.getOrCreate()

# Creating dataframe from list of Row
df = spark.createDataFrame([
	Row(a=1, b='string1', c=date(2021, 1, 1)),
	Row(a=2, b='string2', c=date(2021, 2, 1)),
	Row(a=4, b='string3', c=date(2021, 3, 1))
])

# Printing DataFrame structure
print("DataFrame structure:", df)

# Getting and printing metadata
meta = df.schema.fields
print("Metadata: ", meta)

# Getting list of columns having type
# string or int
# This statement will loop over all the fields
# field.name will return column name and
# field.dataType will return column type
columnList = [field.name for field in df.schema.fields if isinstance(
	field.dataType, StringType) or isinstance(field.dataType, LongType)]
print("Result: ", columnList)
