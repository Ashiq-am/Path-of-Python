import pandas as pd

# read DataFrame
data = pd.read_csv("Customers.csv")

for (Gender, Income), group in data.groupby(['Gender', 'Annual Income(k$)']):
	group.to_csv(f'{Gender} {Income}.csv', index=False)
	print(pd.read_csv(f'{Gender} {Income}.csv'))
