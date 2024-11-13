# Reading the csv file in
# Pyspark DataFrame
df_spark2 = spark.read.option(
'header', 'true').csv("heart.csv")

# Showing the data in the from of
# table and showing only top 5 rows
df_spark2.show(5)
