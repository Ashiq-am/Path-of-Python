# Create a second dataframe
# First set the seed to regenerate the result
from turtle import pd

from pandas import np

np.random.seed(10)

# Create a 5 * 5 dataframe
df2 = pd.DataFrame(np.random.rand(5, 5), columns =['A', 'B', 'C', 'D', 'E'])

df2
