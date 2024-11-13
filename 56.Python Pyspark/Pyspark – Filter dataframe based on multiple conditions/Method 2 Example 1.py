# Using SQL col() function
from pyspark.sql.functions import col
dataframe.filter(col("college") == "DU").show()
