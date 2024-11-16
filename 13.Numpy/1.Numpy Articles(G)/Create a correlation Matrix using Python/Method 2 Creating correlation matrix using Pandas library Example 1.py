import pandas as pd


# collect data
data = {
	'x': [45, 37, 42, 35, 39],
	'y': [38, 31, 26, 28, 33],
	'z': [10, 15, 17, 21, 12]
}

# form dataframe
dataframe = pd.DataFrame(data, columns=['x', 'y', 'z'])
print("Dataframe is : ")
print(dataframe)

# form correlation matrix
matrix = dataframe.corr()
print("Correlation matrix is : ")
print(matrix)
