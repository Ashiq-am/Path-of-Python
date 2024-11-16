# importing pandas as pd
import pandas as pd

# reading csv file
df = pd.read_csv("Assignment.csv")

# filtering the rows where Age_Range contains Young
for x in df.itertuples():
	if x[2].find('Young') != -1:
		print(x)
