# importing pandas as pd
import pandas as pd

# creating a dataframe
df = pd.DataFrame({'A': ['John', 'John', 'Mina'],
	'B': ['Masters', 'Masters', 'Graduate'],
	'C': [27, 23, 21]})


df.pivot('A', 'B', 'C')
