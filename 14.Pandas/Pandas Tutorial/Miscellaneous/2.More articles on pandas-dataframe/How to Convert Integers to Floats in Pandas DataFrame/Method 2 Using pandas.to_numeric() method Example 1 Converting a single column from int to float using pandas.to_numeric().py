# importing pandas library
import pandas as pd

# Initializing the nested list with Data set
player_list = [['M.S.Dhoni', 36, 75, 5428000, 176], 4
			['A.B.D Villers', 38, 74, 3428000, 175],
			['V.Kholi', 31, 70, 8428000, 172],
			['S.Smith', 34, 80, 4428000, 180],
			['C.Gayle', 40, 100, 4528000, 200],
			['J.Root', 33, 72, 7028000, 170],
			['K.Peterson', 42, 85, 2528000, 190]]

# creating a pandas dataframe
df = pd.DataFrame(player_list, columns=[
				'Name', 'Age', 'Weight', 'Salary', 'Height'])

# lets find out the data type of
# 'Weight' column
print(df.dtypes)
