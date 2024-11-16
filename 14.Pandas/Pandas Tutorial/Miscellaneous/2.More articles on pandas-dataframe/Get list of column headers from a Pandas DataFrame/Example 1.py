# importing pandas as pd
import pandas as pd

# creating the dataframe
df = pd.DataFrame({'PassengerId': [892, 893, 894, 895,
								896, 897, 898, 899],
				'PassengerClass': [1, 1, 2, 1, 3, 3, 2, 2],
				'PassengerName': ['John', 'Prity', 'Harry',
									'Smith', 'James', 'Amora',
									'Kiara', 'Joseph'],
				'Age': [32, 54, 71, 21, 37, 9, 11, 54]})

display("The DataFrame :")
display(df)

# print the list of all the column headers
display("The column headers :")
display(list(df.columns.values))
