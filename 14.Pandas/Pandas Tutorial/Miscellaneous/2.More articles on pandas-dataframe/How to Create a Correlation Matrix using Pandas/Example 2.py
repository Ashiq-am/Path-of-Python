import pandas as pd

data = {'A': [45, 37, 42, 50],
		'B': [38, 31, 26, 90],
		'C': [10, 15, 17, 100],
		'D': [60, 99, 23, 56],
		'E': [76, 98, 78, 90]
		}

df = pd.DataFrame(data)

corrM = df.corr()
corrM
