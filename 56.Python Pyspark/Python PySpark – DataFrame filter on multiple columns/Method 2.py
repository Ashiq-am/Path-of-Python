# select dataframe where ID less than
# 3 or name is sridevi and comapny 1
dataframe.where((dataframe.ID < 3) | (
	(dataframe.NAME == 'sridevi') &
(dataframe.Company == 'company 1'))).show()
