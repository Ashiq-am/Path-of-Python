# importing pandas as pd
import pandas as pd

# Creating the First Series
sr1 = pd.Series([22, 18, 19, 20, 21])

# Creating the row axis labels
sr1.index = ['Student 1', 'Student 2', 'Student 3', 'Student 4', 'Student 5']

# Print the series
print(sr1)

# Creating the second Series
sr2 = pd.Series([19, 16, 22, 20, 18])

# Creating the row axis labels
sr2.index = ['Student 1', 'Student 2', 'Student 3', 'Student 4', 'Student 5']

# Print the series
print(sr2)
