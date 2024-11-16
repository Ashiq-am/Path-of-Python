# Creating the MultiIndex
from turtle import pd

from pandas import array

midx = pd.MultiIndex.from_arrays(array,names =('Ranking', 'Names', 'Profession'))

# Print the MultiIndex
print(midx)
