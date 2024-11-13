# Selcet the 'Name' as 'name'
# Select remaining with their original name
data = df.selectExpr("Name as name","DOB","Gender","salary")

# Print the dataframe
data.show()
