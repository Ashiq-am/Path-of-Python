import pandas as pd

# Creating a dictionary to store data
data = {'Name':['Tony', 'Steve', 'Bruce', 'Peter' ] ,
		'Age': [35, 70, 45, 20] }

# Creating DataFrame
df = pd.DataFrame(data)

# Converting dataframe to list
li = df.values.tolist()

# Printing list
print(li)
