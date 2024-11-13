# COnvert PySpark dataframe to pandas
# dataframe
df = df.toPandas()

# Convert the dataframe into
# dictionary
dict = df.to_dict(orient = 'list')

# Print the dictionary
print(dict)
