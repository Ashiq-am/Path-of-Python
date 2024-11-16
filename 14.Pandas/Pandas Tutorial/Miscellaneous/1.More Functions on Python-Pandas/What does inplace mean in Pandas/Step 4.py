# putting inplace=False
new_data_2 = dataframe.rename(columns = {'Name':'FirstName'},
							inplace = False)

#check new_data_2
display(new_data_2)
