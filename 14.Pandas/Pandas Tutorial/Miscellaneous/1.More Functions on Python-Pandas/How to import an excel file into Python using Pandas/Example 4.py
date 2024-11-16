import pandas as pd

df = pd.read_excel('sample.xlsx',
				dtype = {"Products": str,
							"Price":float})
print(df)
