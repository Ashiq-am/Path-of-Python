# without using inplace renaming the column
new_data = dataframe.rename(columns = {'Name':'FirstName'})

# check new_data
display(new_data)
