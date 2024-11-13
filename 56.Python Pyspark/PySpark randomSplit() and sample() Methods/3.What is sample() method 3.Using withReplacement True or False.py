# importing sparksession from pyspark.sql
from pyspark.sql import SparkSession

# to get an existing sparksession
spark = SparkSession.builder.appName
("SparkByExamples.com").getOrCreate()

# taking 100 random records
df = spark.range(100)
print("With Duplicates:")

# to get fraction of record on the basis of seed value
# which may contain duplicates
print(df.sample(True, 0.2, 98).collect())
print("Without Duplicates: ")

# to get fraction of records without redundancy
print(df.sample(False, 0.1, 123).collect())
