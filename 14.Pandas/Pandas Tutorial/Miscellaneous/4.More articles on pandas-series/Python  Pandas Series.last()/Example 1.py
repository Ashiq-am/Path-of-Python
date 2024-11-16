# importing pandas as pd
import pandas as pd

# Creating the Series
sr = pd.Series(['New York', 'Chicago', 'Toronto', 'Lisbon', 'Rio', 'Paris'])

# Create the Index
index_ = pd.date_range('2010-10-09', periods = 6, freq ='2D')

# set the index
sr.index = index_

# Print the series
print(sr)
