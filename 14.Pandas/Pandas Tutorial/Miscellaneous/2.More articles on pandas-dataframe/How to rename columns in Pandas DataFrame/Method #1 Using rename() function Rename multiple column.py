# Import pandas package
import pandas as pd

# Define a dictionary containing ICC rankings
rankings = {'test': ['India', 'South Africa', 'England',
							'New Zealand', 'Australia'],
			'odi': ['England', 'India', 'New Zealand',
							'South Africa', 'Pakistan'],
			't20': ['Pakistan', 'India', 'Australia',
							'England', 'New Zealand']}

# Convert the dictionary into DataFrame
rankings_pd = pd.DataFrame(rankings)

# Before renaming the columns
print(rankings_pd.columns)

rankings_pd.rename(columns = {'test':'TEST', 'odi':'ODI',
							't20':'T20'}, inplace = True)

# After renaming the columns
print(rankings_pd.columns)
