print("Number of null values in column 1 : " +
	str(table.iloc[:, 1].isnull().sum()))
print("Number of null values in column 2 : " +
	str(table.iloc[:, 2].isnull().sum()))
