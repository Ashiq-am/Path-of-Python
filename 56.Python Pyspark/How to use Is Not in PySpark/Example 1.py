from pyspark.sql import SparkSession
from pyspark.sql import Row

spark = SparkSession.builder.appName("GeeksForGeeks").getOrCreate()

data = [
        Row(name="Alpha", age=20, marks=54),
        Row(name="Beta", age=None, marks=None),
        Row(name="Omega", age=17, marks=85),
        Row(name="Sigma", age=None, marks=62)
       ]

df = spark.createDataFrame(data)
df.show()
