# get the ID : not in 1 and 3 from dataframe
dataframe.filter(~(dataframe.ID).isin([1, 3])).show()
