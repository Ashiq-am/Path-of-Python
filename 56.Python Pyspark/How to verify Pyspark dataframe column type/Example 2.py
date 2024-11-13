# finding data type of the Rating
# column using dtype function
data_type = dict(df.dtypes)['Rating']

# printing
print(f'Data type of Rating is : {data_type}')

# visualizing the dataframe
df.show()
