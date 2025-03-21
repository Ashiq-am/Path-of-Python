# import required module
import pandas as pd

# assign data
ipl_data = {'Team': ['Riders', 'Riders', 'Devils', 'Devils',
					'Kings', 'kings', 'Kings', 'Kings',
					'Riders', 'Royals', 'Royals', 'Riders'],
			'Rank': [1, 2, 2, 3, 3, 4, 1, 1, 2, 4, 1, 2],

			'Year': [2014, 2015, 2014, 2015, 2014, 2015, 2016,
					2017, 2016, 2014, 2015, 2017],

			'Points': [876, 789, 863, 673, 741, 812, 756, 788,
					694, 701, 804, 690]}

# create dataframe
df = pd.DataFrame(ipl_data)

# use groupby() to generate sum
df.groupby(['Team']).sum()
