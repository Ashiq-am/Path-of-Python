# Importing the library
import pandas as pd
from sklearn.preprocessing import StandardScaler


# Creating the data frame
details = {
	'col1': [1, 3, 5, 7, 9],
	'col2': [7, 4, 35, 14, 56]
}

# creating a Dataframe object
df = pd.DataFrame(details)

# define standard scaler
scaler = StandardScaler()

# transform data
df = scaler.fit_transform(df)
