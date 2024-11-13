# filter rows where ID greater than 2
# and college is vvit
dataframe.where((dataframe.ID>'2') & (dataframe.college=='vvit')).show()
