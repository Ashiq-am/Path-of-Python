# Importing libraries
import pandas as pd
import numpy as np

# Initializing the nested list with Data set
player_list = [['M.S.Dhoni', 36, 75, 5428000],
			[np.nan, 36, 74, np.nan],
			['V.Kholi', 31, 70, 8428000],
			['S.Smith', 34, 80, 4428000],
			[pd.NaT, 39, 100, np.nan],
			[np.nan, 33, 90.5, 7028000],
			['K.Peterson', 42, 85, pd.NaT]]

# creating a pandas dataframe
df = pd.DataFrame(player_list, columns=['Name', 'Age',
										'Weight', 'Salary'])

df
