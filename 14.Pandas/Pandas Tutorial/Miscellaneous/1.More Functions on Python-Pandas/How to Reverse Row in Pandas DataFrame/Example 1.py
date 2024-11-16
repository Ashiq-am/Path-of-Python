# Import pandas package
import pandas as pd

# Define a dictionary containing employee data
data = {'Income': [150000, 13000, 11000, 11000],
		'Expences': [10000, 11000, 7000, 50000],
		'Profit': [5000, 2000, 4000, 6000]
		}


# Convert the dictionary into DataFrame
dataframe = pd.DataFrame(data)

# Observe the result
dataframe
