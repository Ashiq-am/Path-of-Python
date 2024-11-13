# import the functions as F from pyspark.sql
import pyspark.sql.functions as F
from pyspark.sql.types import IntegerType

# define the sum_col
def sum_col(b, c, d):
	col_sum = b+c+d
	return col_sum

# integer datatype is defined
new_f = F.udf(sum_col, IntegerType())

# calling and creating the new
# col as udf_method_sum
df_col1 = data.withColumn("Udf_method_sum",
						new_f("B", "C", "D"))

# Showing and printing the schema of the Dataframe
df_col1.printSchema()
df_col1.show()
