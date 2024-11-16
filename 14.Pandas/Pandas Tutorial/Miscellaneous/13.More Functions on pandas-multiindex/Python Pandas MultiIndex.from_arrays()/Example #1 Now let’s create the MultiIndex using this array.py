# Creating the MultiIndex
from turtle import pd

from pandas import array

midx = pd.MultiIndex.from_arrays(array,names =('Number', 'Names'))

# Print the MultiIndex
print(midx)
