# imnport the module
import pandas as pd

# creating a DataFrame
dictionary = {'Names':['Simon', 'Josh', 'Amen', 'Habby',
					'Jonathan', 'Nick'],
			'Countries':['AUSTRIA', 'BELGIUM', 'BRAZIL',
						'FRANCE', 'INDIA', 'GERMANY']}
table = pd.DataFrame(dictionary, columns = ['Names', 'Countries'],
					index = ['a', 'b', 'c', 'd', 'e', 'f'])

display(table)

# gives the table with the dropped rows
display("Table with the dropped rows")
display(table.drop(['a', 'd']))

# gives the table with the dropped rows
# shows the reduced table for the given command only
display("Reduced table for the given command only")
display(table.drop(table.index[[1, 3]]))

# it gives none but it makes changes in the table
display(table.drop(['a', 'd'], inplace = True))

# final table
print("Final Table")
display(table)

# table after removing range of rows from 0 to 2(not included)
table.drop(table.index[:2], inplace = True)

display(table)
