# importing pandas as pd
import pandas as pd

# Creating the first dataframe
df1 = pd.DataFrame({"A":[1, 5, 3, 4, 2],
					"B":[3, 2, 4, 3, 4],
					"C":[2, 2, 7, 3, 4],
					"D":[4, 3, 6, 12, 7]},
				index =["A1", "A2", "A3", "A4", "A5"])

# Creating the second dataframe
df2 = pd.DataFrame({"A":[10, 11, 7, 8, 5],
					"B":[21, 5, 32, 4, 6],
					"C":[11, 21, 23, 7, 9],
					"D":[1, 5, 3, 8, 6]},
					index =["A1", "A2", "A3", "A4", "A5"])

# perform modulus of df2 by df1
df1.rmod(df2)
