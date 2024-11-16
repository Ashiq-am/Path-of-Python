# impporting the module
import pandas as pd

# creating a DataFrame
dictionary = {'Names':['Simon', 'Josh', 'Amen', 'Habby',
					'Jonathan', 'Nick', 'Jake'],
			'Countries':['AUSTRIA', 'BELGIUM', 'BRAZIL',
						'JAPAN', 'FRANCE', 'INDIA', 'GERMANY'],
			'Boolean':[True, False, False, True,
						True, False, True],
			'HouseNo':[231, 453, 723, 924, 784, 561, 403],
			'Location':[12.34, 45.67, 03.45, 17.23,
						83.12, 90.45, 84.34]}
table = pd.DataFrame(dictionary, columns = ['Names', 'Countries',
											'Boolean', 'HouseNo', 'Location'])

print("Data Types of The Columns in Data Frame")
display(table.dtypes)

print("Data types on accessing a single column of the Data Frame ")
print("Type of Names Column : ", type(table.iloc[:, 0]))
print("Type of HouseNo Column : ", type(table.iloc[:, 3]), "\n")

print("Data types of individual elements of a particular columns Data Frame ")
print("Type of Names Column Element : ", type(table.iloc[:, 0][1]))
print("Type of Boolean Column Element : ", type(table.iloc[:, 2][2]))
print("Type of HouseNo Column Element : ", type(table.iloc[:, 3][4]))
print("Type of Location Column Element : ", type(table.iloc[:, 4][0]))
