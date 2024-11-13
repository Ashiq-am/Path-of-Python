from pyspark.sql import SparkSession
from pyspark.sql.types import IntegerType, StringType
from pyspark.sql.functions import udf

spark = SparkSession.builder.appName('UDF PRACTICE').getOrCreate()

cms = ["Name", "RawScore"]
data = [("Jack", "79"),
        ("Mira", "80"),
        ("Carter", "90")]

df = spark.createDataFrame(data=data, schema=cms)

df.show()
