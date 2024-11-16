import pandas as pd

# read the dataset as csv file
data = pd.read_csv('Titanic.csv')

# drop the name column as it is of no importance here
data.drop('Name', axis=1, inplace=True)

# view the first 5 rows of the titanic dataset
data.head()
