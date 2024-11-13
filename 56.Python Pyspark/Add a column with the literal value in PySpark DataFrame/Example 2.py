# this will create a temp view of the table as lit_val
df2.createOrReplaceTempView("temp")

# select all the columns and rows
# from data table and insert new
# columns 'literal_values_2' with values 2
df2 = spark.sql("select *, 2 as literal_values_2 from temp")

# showing the schema and updated table
df2.printSchema()
df2.show()
