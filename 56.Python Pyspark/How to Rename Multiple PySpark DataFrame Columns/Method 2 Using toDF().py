# display actual
print("Actual columns: ", dataframe.columns)

# change column names to A,B,C
dataframe = dataframe.toDF(*("A", "B", "C"))

# display new columns
print("New columns: ", dataframe.columns)

# display dataframe
dataframe.show()
