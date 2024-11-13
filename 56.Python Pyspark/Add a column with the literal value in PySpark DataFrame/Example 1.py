# Import the lit() function
# from the pyspark.sql.functions
from pyspark.sql.functions import lit

# select all the columns from data
# table and insert new columns
# 'literal_values_1' with values 1
df2 = data.select('*' ,lit("1").alias("literal_values_1"))

# showing the schema and updated table
df2.printSchema()
df2.show()
