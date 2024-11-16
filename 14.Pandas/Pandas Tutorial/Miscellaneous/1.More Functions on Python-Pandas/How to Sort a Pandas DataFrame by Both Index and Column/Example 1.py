# import necessary packages
import pandas as pd

# create 2 dataframes with diferent indexes
hostelCandidates1 = pd.DataFrame({'col2': [150, 170, 160],
								'col1': [70, 55, 60]},
								index=[3, 2, 1])
print('original DataFrame')
print(hostelCandidates1)

# sorted temperorle based on index labels
print('Sorted by index')
hostelCandidates1.sort_index(axis=0)
