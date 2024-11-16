# reindex the columns
# we fill the missing values using ffill method
df.reindex_axis(["A", "B", "D", "E"], axis = 1, method ='ffill')
