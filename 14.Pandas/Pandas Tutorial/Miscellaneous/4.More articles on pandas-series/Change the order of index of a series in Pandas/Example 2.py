# import required library
import pandas as pd
import numpy as np

# create numpy array
data = np.array(["Android dev",
				"content writing",
				"competetive coding"])
# create a series
total_series = pd.Series(data,
						index = [1, 2, 3])
# reindexing of series
total_series = total_series.reindex([2, 3, 1])

# show the series
total_series
