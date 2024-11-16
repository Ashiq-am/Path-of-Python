# set required index
index_set = data.columns.get_loc('E-mail')
index_gmail = data.columns.get_loc('Google-mail')
index_yahoo = data.columns.get_loc('Yahoo-mail')

print(index_set, index_gmail,
	index_yahoo)
