# get ID except 1
dataframe.where(~(dataframe.ID).isin([1])).show()
