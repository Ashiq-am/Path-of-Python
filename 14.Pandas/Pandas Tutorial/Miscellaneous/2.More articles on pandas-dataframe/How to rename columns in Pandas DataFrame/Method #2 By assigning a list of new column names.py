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

rankings_pd.columns = ['TEST', 'ODI', 'T-20']

# After renaming the columns
print(rankings_pd.columns)
