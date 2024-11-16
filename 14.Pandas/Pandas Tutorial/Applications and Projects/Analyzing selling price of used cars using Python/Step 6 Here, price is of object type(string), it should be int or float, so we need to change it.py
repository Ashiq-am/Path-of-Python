data.price.unique()

# Here it contains '?', so we Drop it
data = data[data.price != '?']

# checking it again
data.dtypes
