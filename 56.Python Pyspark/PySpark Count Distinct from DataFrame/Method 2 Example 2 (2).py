# using the SQL query to count distinct
# records in 2 columns only display the
# count on the screen
spark.sql("select count(distinct(Emp_name, Salary)) from df2").show()
