# import expr from the functions
from pyspark.sql.functions import expr

# create the new column as by withcolumn
# by giving argument as
# col_name ='expression_method_sum'
# and expr() function which
# will take expressions argument as string
df_col1 = df_col1.withColumn('expression_method_sum',
							expr("B+C + D"))

# Showing and printing the schema of
# the Dataframe
df_col1.printSchema()
df_col1.show()
