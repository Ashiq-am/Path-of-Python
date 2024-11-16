# Passed a dictionary to astype() function
df = df.astype({"Name":'category', "Age":'int64'})

# Now print the data type
# of all columns after change
df.info()
