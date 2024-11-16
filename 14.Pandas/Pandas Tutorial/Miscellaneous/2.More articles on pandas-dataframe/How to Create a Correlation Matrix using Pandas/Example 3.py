import pandas as pd

# Integer and string values can
# never be correlated.
data = {'A': [45, 37, 42, 50],
		'B': ['R', 'O', 'M', 'Y'],
		}

df = pd.DataFrame(data)

corrM = df.corr()
corrM
