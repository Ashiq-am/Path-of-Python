# import Dataframe class
# from pandas library
from pandas import DataFrame

# import numpy library
import numpy as np

# dictionary
Myvalue = {'DATA ENTRY':[4.834327, 5.334477,
						6.89, 7.6454, 8.9659] }
# create a Dataframe
df = DataFrame(Myvalue,
			columns = ['DATA ENTRY'])

# Rounding of Value to its Floor value
rounddown = df['DATA ENTRY'].apply(np.floor)

# show the rounded value
rounddown
