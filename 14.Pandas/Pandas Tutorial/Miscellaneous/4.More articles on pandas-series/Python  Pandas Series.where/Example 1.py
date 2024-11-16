# importing pandas as pd
import pandas as pd

# Creating the First Series
sr1 = pd.Series(['New York', 'Chicago', 'Toronto', 'Lisbon', 'Rio'])

# Creating the row axis labels
sr1.index = ['City 1', 'City 2', 'City 3', 'City 4', 'City 5']

# Print the series
print(sr1)

# Creating the second Series
sr2 = pd.Series(['New York', 'Bangkok', 'London', 'Lisbon', 'Brisbane'])

# Creating the row axis labels
sr2.index = ['City 1', 'City 2', 'City 3', 'City 4', 'City 5']

# Print the series
print(sr2)
