# importing pandas as pd
import pandas as pd

# Creating the dataframe
df = pd.DataFrame({"A":[10, 11, 7, 8, 5],
				"B":[21, 5, 32, 4, 6],
				"C":[11, 21, 23, 7, 9],
				"D":[1, 5, 3, 8, 6]},
				index =["A1", "A2", "A3", "A4", "A5"])

# Print the dataframe
df
