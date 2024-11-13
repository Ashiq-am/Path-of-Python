# importing module
import pyspark

# importing sparksession from pyspark.sql module and Row module
from pyspark.sql import SparkSession,Row

# creating sparksession and giving an app name
spark = SparkSession.builder.appName('sparkdf').getOrCreate()

# list of college data
dataframe = spark.createDataFrame([Row("vignan"),
								Row("rvrjc"),
								Row("klu"),
								Row("rvrjc"),
								Row("klu"),
								Row("vignan"),
								Row("iit")],
								["college"])

# display dataframe
dataframe.show()
