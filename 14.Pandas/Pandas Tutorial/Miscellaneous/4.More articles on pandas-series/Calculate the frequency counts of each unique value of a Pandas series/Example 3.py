# importing pandas as pd
import pandas as pd

# creating the Series
sr = pd.Series(['Mumbai', 'Pune', 'Agra', 'Pune', 'Goa', 'Shimla', 'Goa', 'Pune'])

# displaying the series
print(sr)

# finding the unique count
sr.value_counts()
