# inner join on two dataframes
# and remove duplicate column
dataframe.join(dataframe1,
			dataframe.ID == dataframe1.ID,
			"inner").drop(dataframe.ID).show()
