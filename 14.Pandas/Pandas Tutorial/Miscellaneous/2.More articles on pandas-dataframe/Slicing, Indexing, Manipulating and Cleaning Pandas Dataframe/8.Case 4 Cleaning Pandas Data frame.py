# importing pandas and Numpy libraries
import pandas as pd
import numpy as np

# Initializing the nested list with Data set
player_list = [['M.S.Dhoni', 36, 75, 5428000],
			['A.B.D Villers', np.nan, 74, np.nan],
			['V.Kholi', 31, 70, 8428000],
			['S.Smith', 34, 80, 4428000],
			['C.Gayle', np.nan, 100, np.nan],
			[np.nan, 33, np.nan, 7028000],
			['K.Peterson', 42, 85, 2528000]]

# creating a pandas dataframe
df = pd.DataFrame(player_list, columns=['Name', 'Age', 'Weight', 'Salary'])

df
