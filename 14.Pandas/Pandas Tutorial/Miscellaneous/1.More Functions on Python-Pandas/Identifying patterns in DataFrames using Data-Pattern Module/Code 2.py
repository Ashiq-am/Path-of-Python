# importing the data_patterns module
import data_patterns


# importing the pandas module
import pandas as pd


# creating a pandas dataframe
df = pd.DataFrame(columns=['Name', 'Grade', 'value1',
						'Value2', 'Value3', 'Value4', 'value5'],
				data=[['Alpha', 'A', 1000, 800, 0, 200, 200],
						['Beta', 'B', 4000, 0, 3200, 800, 800],
						['Gama', 'A', 800, 0, 700, 100, 100],
						['Theta', 'B', 2500, 1800, 0, 700, 700],
						['Ceta', 'C', 2100, 0, 2200, 200, 200],
						['Saiyan', 'C', 9000, 8800, 0, 200, 200],
						['SSai', 'A', 9000, 0, 8800, 200, 200],
						['SSay', 'A', 9000, 8800, 0, 200, 200],
						['Geeks', 'A', 9000, 0, 8800, 200, 200],
						['SsBlue', 'B', 9000, 0, 8800, 200, 19]])

# setting datag=frame index
df.set_index('Name', inplace=True)


# creating a pattern mixer object
miner = data_patterns.PatternMiner(df)


# finding the pattern in the datframe
# name is optional
# other patterns which can be used ‘>’, ‘<’, ‘<=’, ‘>=’, ‘!=’, ‘sum’
df_patterns = miner.find({'name': 'equal values',
						'pattern': '=',
						'parameters': {"min_confidence": 0.5,
										"min_support": 2,
										"decimal": 8}})


# getting the analyized dataframe
df_results = miner.analyze(df)


# prinitng the analyized results
print(df_results)
