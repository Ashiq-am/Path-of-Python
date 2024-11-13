# count ID column where ID > 4
# and sector is sales or IT
dataframe.select('ID').where((dataframe.ID>4) &
							((dataframe.sector=='sales')|
							(dataframe.sector=='IT'))).count()
