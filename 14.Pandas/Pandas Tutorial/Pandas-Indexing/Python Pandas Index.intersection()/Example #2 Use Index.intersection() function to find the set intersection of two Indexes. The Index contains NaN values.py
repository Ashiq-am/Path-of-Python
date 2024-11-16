# importing pandas as pd
import pandas as pd

# Creating the first Index
idx1 = pd.Index(['2015-10-31', '2015-12-02', None, '2016-01-03',
					'2016-02-08', '2017-05-05', '2014-02-11'])

# Creating the second Index
idx2 = pd.Index(['2015-10-31', '2015-10-02', '2018-01-03',
		'2016-02-08', '2017-06-05', '2014-07-11', None])

# Print the first and second Index
print(idx1, '\n', idx2)
