# filling the missing values using ffill method
df.reindex_axis(["A1", "A2", "A4", "A7", "A8"],
					axis = 0, method ='ffill')
