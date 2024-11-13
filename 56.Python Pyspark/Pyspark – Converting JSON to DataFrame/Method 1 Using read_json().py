# import pandas to read json file
import pandas as pd

# importing module
import pyspark

# importing sparksession from pyspark.sql module
from pyspark.sql import SparkSession

# creating sparksession and giving an app name
spark = SparkSession.builder.appName('sparkdf').getOrCreate()


# creating a dataframe from the json file named student
dataframe = spark.createDataFrame(pd.read_json('student.json'))

# display the dataframe (Pyspark dataframe)
dataframe.show()
