# Creating the temporary view
# of the DataFrame as temp.
df_col1 = df_col1.createTempView("temp")

# By using sql calause creating
# new columns as sql_method
df_col1=spark.sql('select *, B+C+D as sql_method from temp')

# Printing the schema of the dataFrame
# and showing the DataFrame
df_col1.printScheam()
df_col1.show()
