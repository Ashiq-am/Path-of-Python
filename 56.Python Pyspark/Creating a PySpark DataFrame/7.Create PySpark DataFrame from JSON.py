# Need to import to use date time
from datetime import datetime, date

# need to import for working with pandas
import pandas as pd

# need to import to use pyspark
from pyspark.sql import Row

# need to import for session creation
from pyspark.sql import SparkSession

# creating the session
spark = SparkSession.builder.getOrCreate()

# PySpark DataFrame from a csv
df = spark.createDataFrame(pd.read_json('data.json'))
df

# show table
df.show()

# show schema
df.printSchema()
