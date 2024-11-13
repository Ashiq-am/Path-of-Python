# Rename the column name 'Gender' to 'Sex'
# Then for the returning dataframe
# again rename the 'salary' to 'Amount'
df.withColumnRenamed("Gender","Sex").withColumnRenamed("salary","Amount").show()
