import pandas
import pandas as pd

# from pyspark library import
# SparkSession
from pyspark.sql import SparkSession

# Building the SparkSession and name
# it :'pandas to spark'
spark = SparkSession.builder.appName(
    "pandas to spark").getOrCreate()

# Create the DataFrame with the help
# of pd.DataFrame()
data = pd.DataFrame({'State': ['Alaska', 'California',
                               'Florida', 'Washington'],

                     'city': ["Anchorage", "Los Angeles",
                              "Miami", "Bellevue"]})

# enableing the Apache Arrow for converting
# Pandas to pySpark DF(DataFrame)
spark.conf.set("spark.sql.execution.arrow.enabled", "true")

# Creating the DataFrame
sprak_arrow = spark.createDataFrame(data)

# Show the DataFrame
sprak_arrow.show()
