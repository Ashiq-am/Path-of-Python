# import Dataframe from
# pandas library
from pandas import DataFrame

# import numpy
import numpy as np

# dictionary
Myvalue = {'DATA ENTRY': [4.834327, 5.334477,
						6.89, 7.6454, 8.9659]}

# create a Dataframe
df = DataFrame(Myvalue,
			columns = ['DATA ENTRY'])

# Here we are rounding the
# value to its ceiling values
roundUp = df['DATA ENTRY'].apply(np.ceil)

# show the rounded value
roundUp
