# Creating the MultiIndex
from turtle import pd

midx = pd.MultiIndex.from_tuples(tuples, names =('Age', 'Name'))

# Print the MultiIndex
print(midx)
