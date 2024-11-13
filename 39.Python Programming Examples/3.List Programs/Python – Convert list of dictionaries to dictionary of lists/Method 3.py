#import pandas
import pandas as pd

# consider the list of dictionary
data = [{'manoj': 'java', 'bobby': 'python'},
		{'manoj': 'php', 'bobby': 'java'},
		{'manoj': 'cloud', 'bobby': 'big-data'}]

# convert into dictionary of list
# with list as values using pandas dataframe
pd.DataFrame(data).to_dict(orient="list")
