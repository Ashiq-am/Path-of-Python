# filter rows where ID greater
# than 2 and college is vignan
dataframe.filter((dataframe.ID>'2') & (dataframe.college=='vignan')).show()
