# import pandas module
import pandas as pd

# create first dataframe
data1 = pd.DataFrame({'name': ['sravan', 'bobby',
							'ojaswi', 'rohith',
							'gnanesh'],
					'subjects': ['java', 'python',
								'php', 'java', '.NET']})

# create second dataframe
data2 = pd.DataFrame({'name': ['gopi', 'harsha', 'ravi',
							'uma', 'deepika'],
					'subjects': ['c/c++', 'html/css',
								'dbms', 'java', 'IOT']})

# stack the two DataFrames
pd.concat([data1, data2], ignore_index=True, axis=0)
