# import the functions as F from pyspark.sql
import pyspark.sql.functions as F
from pyspark.sql.types import IntegerType

# define the sum_col
def Total(Course_Fees, Discount):
	res = Course_Fees - Discount
	return res

# integer datatype is defined
new_f = F.udf(Total, IntegerType())

# calling and creating the new
# col as udf_method_sum
new_df = df.withColumn(
"Total_price", new_f("Course_Fees", "Discount"))

# Showing the Dataframe
new_df.show()
