#import the libraries
from pyspark.sql.types import LongType, StringType, StructField, StructType
from pyspark.sql.functions import col

#define the schema
struct_schema = StructType([
	StructField("Street_name", StringType()),
	StructField("city_name", StringType()),
	StructField("Zip_code", IntegerType())
])
#apply the schema
df.select(col("address").cast(struct_schema)).printSchema()
