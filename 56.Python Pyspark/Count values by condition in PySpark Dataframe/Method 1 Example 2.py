# count values in all column count
# where ID greater than 3 and sector = IT
dataframe.select().where((dataframe.ID>3) &
						(dataframe.sector=='IT')).count()
