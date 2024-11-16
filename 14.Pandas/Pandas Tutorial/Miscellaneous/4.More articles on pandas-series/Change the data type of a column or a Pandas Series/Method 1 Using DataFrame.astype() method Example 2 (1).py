# creating a dictionary
# with column name and data type
data_types_dict = {'id': str}

# we will change the data type
# of id column to str by giving
# the dict to the astype method
df = df.astype(data_types_dict)

# checking the data types
# using df.dtypes method
df.dtypes
