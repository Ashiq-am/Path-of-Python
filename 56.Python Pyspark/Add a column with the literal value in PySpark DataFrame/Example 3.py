# import the udf from pyspark
from pyspark.sql.functions import udf

# defining the data types of udf which is
# integer type
@udf("int")

# defining the lit_col() function which
# will return literal values to data frame
def lit_col():
	return 3

# create new column as
# 'literal_values_3' with values 3
df2 = df2.withColumn('literal_values_3', lit_col())

# showing the schema and updated table
df2.printSchema()
df2.show()
