# set index
index_set = data.columns.get_loc('Description')
index_time = data.columns.get_loc('New time')

print(index_set, index_time)
