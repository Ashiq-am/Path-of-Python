# Drop NewCases, NewDeaths, NewRecovered rows from dataset1

dataset1.drop(['NewCases', 'NewDeaths', 'NewRecovered'],
			axis=1, inplace=True)

# Select random set of values from dataset1
dataset1.sample(5)
