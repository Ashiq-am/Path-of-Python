# Importing Required Libraries
import pandas as pd
import random

# Creating data for main dataframe
from IPython.core.display import display

col1 = [random.randint(1, 9) for i in range(15)]
col2 = [random.random() for i in range(15)]
col3 = [random.choice(['Geeks', 'of', 'Computer', 'Science'])
		for i in range(15)]
col4 = [random.randint(1, 9) for i in range(15)]
col5 = [random.randint(1, 9) for i in range(15)]

# Defining Column name for main dataframe
data_generated = {
	'value1': col1,
	'value2': col2,
	'value3': col3,
	'value4': col4,
	'value5': col5
}

# Creating the datafram using DataFrame() function
print("First data frame")
dataframe = pd.DataFrame(data_generated)
display(dataframe)

# Creating a second dataframe that will be the subset of main dataframe
print("Second data frame")
dataframe_second = dataframe[['value1', 'value2', 'value3']].sample(n=4)
display(dataframe_second)

# Rows of a dataframe using the indices of another dataframe
print("selecting rows of first datafame using second dataframe")
display(dataframe.loc[dataframe_second.index])
