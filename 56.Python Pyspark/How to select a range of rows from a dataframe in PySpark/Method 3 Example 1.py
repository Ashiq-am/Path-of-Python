# create view for the dataframe
dataframe.createOrReplaceTempView("my_view")

# data subject1 between 23 and 78
spark.sql("SELECT * FROM my_view WHERE\
subject1 between 23 and 78").collect()
