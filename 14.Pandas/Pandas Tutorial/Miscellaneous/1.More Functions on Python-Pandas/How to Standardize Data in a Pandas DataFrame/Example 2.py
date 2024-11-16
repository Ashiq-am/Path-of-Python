# Importing the library
import pandas as pd
import scipy
from scipy import stats


# Creating the data frame
details = {
	'col1': [1, 3, 5, 7, 9],
	'col2': [7, 4, 35, 14, 56]
}

# creating a Dataframe object
df = pd.DataFrame(details)

# Z-Score using scipy
df['col2'] = stats.zscore(df['col2'])
