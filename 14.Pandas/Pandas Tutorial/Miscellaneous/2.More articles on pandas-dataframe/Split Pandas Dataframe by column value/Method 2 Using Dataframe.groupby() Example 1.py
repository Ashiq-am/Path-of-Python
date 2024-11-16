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
# on basis of 'Salary' column values
# using dataframe.groupby() function
df1, df2 = [x for _, x in df.groupby(df['Salary'] < 4528000)]

# printing df1
df1
