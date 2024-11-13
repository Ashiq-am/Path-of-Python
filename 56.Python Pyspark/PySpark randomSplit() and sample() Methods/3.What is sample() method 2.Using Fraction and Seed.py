# importing sparksession from pyspark.sql
from pyspark.sql import SparkSession

# to get an existing sparksession
spark = SparkSession.builder.appName
("SparkByExamples.com").getOrCreate()

# taking random 100 records
df = spark.range(100)

# to get fraction of records on the basis of seed value
print(df.sample(0.1, 97).collect())
