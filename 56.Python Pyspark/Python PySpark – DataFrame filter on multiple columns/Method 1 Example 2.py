# select dataframe where ID less than
# 3 or name is sridevi
dataframe.filter((dataframe.ID < 3) |
				(dataframe.NAME == 'sridevi')).show()
