# importing pandas as pd
import pandas as pd

# Creating the dataframe
df = pd.DataFrame({"A":[1, 5 + 1j, 3+.2j, 4 + 1j, None],
				"B":[3, 2, 4, 3, 4],
				"C":["brook", "daniela", "samantha", "hayden", "nathan"],
				"D":[None, 3, 6, None, 7]},
				index =["A1", "A2", "A3", "A4", "A5"])

# Print the dataframe
df
