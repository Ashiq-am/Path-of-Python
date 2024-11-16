# Import pandas
import pandas as pd

# Create a DataFrame
df1 = {'Name':['George', 'Andrea', 'John', 'Helen',
			'Ravi', 'Julia', 'Justin'],
	'EnglishScore':[62, 47, 55, 74, 32, 77, 86]}

df1 = pd.DataFrame(df1, columns = ['Name', ''])

# Sorting the DataFrame in Ascending Order of English Score
df1.sort_values(by =['EnglishScore'], inplace = True)
