# code
import pandas as pd

# Create a DataFrame
df1 = {'Name':['George', 'Andrea', 'John', 'Helen',
			'Ravi', 'Julia', 'Justin'],
	'EnglishScore':[62, 47, 55, 74, 32, 77, 86]}

df1 = pd.DataFrame(df1, columns =['Name', 'EnglishScore'])

# Sorting the DataFrame in Ascending Order of English Score
# Sorting just for the purpose of better data readibility.
df1.sort_values(by =['EnglishScore'], inplace = True)

# Calculating Quantile Rank
df1['QuantileRank']= pd.qcut(df1['EnglishScore'], q = 4, labels = False)

# Calculating Decile Rank
df1['DecileRank'] = pd.qcut(df1['EnglishScore'], q = 10, labels = False)

# printing the datafarame
print(df1)
