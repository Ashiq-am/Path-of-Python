# import necessary packages
import pandas as pd

# create 2 dataframes with diferent indexes
hostelCandidates1 = pd.DataFrame({'Height in CMs': [150, 170, 160],
								'Weight in KGs': [70, 55, 60]},
								index=[1, 2, 3])

hostelCandidates2 = pd.DataFrame({'Height in CMs': [150, 170, 160],
								'Weight in KGs': [70, 55, 60]},
								index=['A', 'B', 'C'])

# displaying 2 dataframes
print(hostelCandidates1)
print(hostelCandidates2)

# compare 2 dataframes
hostelCandidates1 == hostelCandidates2
