# importing pandas library
import pandas as pd

# Initializing the nested list with Data-set
player_list = [['M.S.Dhoni', 36, 75, 5428000],
			['A.B.D Villers', 38, 74, 3428000],
			['V.Kholi', 31, 70, 8428000],
			['S.Smith', 34, 80, 4428000],
			['C.Gayle', 40, 100, 4528000],
			['J.Root', 33, 72, 7028000],
			['K.Peterson', 42, 85, 2528000]]

# creating a pandas dataframe
df = pd.DataFrame(player_list,
				columns = ['Name', 'Age',
							'Weight', 'Salary'])

# splitting the dataframe into 2 parts
# on basis of 'Weight' column values
mask = df['Weight'] >= 80

df1 = df[mask]

# invert the boolean values
df2 = df[~mask]

# printing df1
df1
