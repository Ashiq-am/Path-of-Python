list = ['Employee ID','Employee NAME','Company Name']

# delete two columns
dataframe = dataframe.drop(*list)
dataframe.show()
