# count values in NAME column
# where ID greater than 5
dataframe.select('NAME').where(dataframe.ID>5).count()
