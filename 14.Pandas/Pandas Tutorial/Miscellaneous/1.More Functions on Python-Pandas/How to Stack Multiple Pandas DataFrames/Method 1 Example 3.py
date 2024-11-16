# import pandas module
import pandas as pd

# create first dataframe
data1 = pd.DataFrame({'name': ['sravan', 'bobby', 'ojaswi',
							'rohith', 'gnanesh'],
					'subjects': ['java', 'python',
								'php', 'java', '.NET']})

# create second dataframe
data2 = pd.DataFrame({'name': ['gopi', 'harsha', 'ravi',
							'uma', 'deepika'],
					'subjects': ['c/c++', 'html/css',
								'dbms', 'java', 'IOT']})

# create third dataframe
data3 = pd.DataFrame(
	{'name': ['ragini', 'latha'], 'subjects': ['java', 'python']})

# create forth dataframe
data4 = pd.DataFrame(
	{'name': ['gowri', 'jyothika'], 'subjects': ['java', 'IOT']})

# stack the four DataFrames horizontally
pd.concat([data1, data2, data3, data4], axis=1, ignore_index=True)
