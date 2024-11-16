# importing the module
import pandas as pd

# creating the series
series = pd.Series(['g', 'e', 'e', 'k', 's',
					'f', 'o', 'r',
					'g', 'e', 'e', 'k', 's'])

# counting the frequency of each element
freq = series.value_counts()

# replacing everything else as Other
series[~series.isin(freq .index[:1])] = None
print(series)
