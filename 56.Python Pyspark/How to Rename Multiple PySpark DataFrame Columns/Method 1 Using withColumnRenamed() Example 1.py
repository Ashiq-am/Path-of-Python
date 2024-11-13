# display actual columns
print("Actual columns: ", dataframe.columns)

# change the college column name to university
# and ID to student_id
dataframe = dataframe.withColumnRenamed(
"college", "university").withColumnRenamed("ID", "student_id")

# display modified columns
print("modified columns: ", dataframe.columns)

# final dataframe
dataframe.show()
