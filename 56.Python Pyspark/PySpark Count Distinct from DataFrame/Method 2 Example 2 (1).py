# creating a temporary view of
# Dataframe and storing it into df2
df.createOrReplaceTempView("df2")

# using the SQL query to count all
# distinct records and display the
# count on the screen
spark.sql("select count(distinct(*)) from df2").show()
