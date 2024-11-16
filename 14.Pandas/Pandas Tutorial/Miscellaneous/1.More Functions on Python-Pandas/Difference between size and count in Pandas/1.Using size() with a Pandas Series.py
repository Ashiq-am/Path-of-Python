import pandas as pd

data = {'A': [1, 2, 3, None, 5]}
series = pd.Series(data['A'])

total_size = series.size
print(total_size)
