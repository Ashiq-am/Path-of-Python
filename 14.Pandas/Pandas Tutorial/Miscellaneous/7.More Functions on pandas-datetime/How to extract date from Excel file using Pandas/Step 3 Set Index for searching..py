# set required index
index_set = data.columns.get_loc('Description')
index_date = data.columns.get_loc('new_Date')

print(index_set, index_date)
