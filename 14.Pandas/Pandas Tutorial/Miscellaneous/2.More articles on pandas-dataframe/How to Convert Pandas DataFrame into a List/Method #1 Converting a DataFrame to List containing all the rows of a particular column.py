import pandas as pd

# Creating a dictionary to store data
data = {'Name':['Tony', 'Steve', 'Bruce', 'Peter' ] ,
		'Age': [35, 70, 45, 20] }

# Creating DataFrame
df = pd.DataFrame(data)

# Convering DataFrame to a list containg
# all the rows of column 'Name'
names = df['Name'].tolist()

# Printing the converted list.
print(names)
