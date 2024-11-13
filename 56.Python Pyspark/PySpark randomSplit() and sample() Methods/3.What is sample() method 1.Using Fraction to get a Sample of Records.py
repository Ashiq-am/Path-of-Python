# importing sparksession from pyspark.sql
from pyspark.sql import SparkSession

# to get an existing sparksession
spark = SparkSession.builder.appName
("SparkByExamples.com").getOrCreate()

# taking random 100 records
df = spark.range(100)

# to get 5% records out of total records
print(df.sample(0.05).collect())
