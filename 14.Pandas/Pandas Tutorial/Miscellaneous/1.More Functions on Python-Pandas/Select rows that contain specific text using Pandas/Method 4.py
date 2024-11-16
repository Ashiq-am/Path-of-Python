# using regular expressions
from re import search

# import pandas as pd
import pandas as pd

# reading CSV file
df = pd.read_csv("Assignment.csv")

# iterating over rows with job as Govt and printing
for ind in df.index:
	if search('Govt', df['job'][ind]):
		print(df['job'][ind], df['Savings'][ind],
			df['Age_Range'][ind], df['Credit-Rating'][ind])
