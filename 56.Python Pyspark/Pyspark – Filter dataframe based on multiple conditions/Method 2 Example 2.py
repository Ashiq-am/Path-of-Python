# Using SQL col() function
from pyspark.sql.functions import col


dataframe.filter((col("college") == "DU") &
				(col("student_NAME") == "Amit")).show()
