import pandas as pd

data = {'A': [1, 2, 3, None, 5],
		'B': [6, 7, None, 9, 10]}
df = pd.DataFrame(data)

count_valid = df.count()
print(count_valid)
