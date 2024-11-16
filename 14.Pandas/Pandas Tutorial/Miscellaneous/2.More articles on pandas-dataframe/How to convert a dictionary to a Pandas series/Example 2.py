# Import pandas library
import pandas as pd

# Create a dictionary
d = {'a' : 10, 'b' : 20,
	'c' : 40, 'd' :80,
	'e' :160}


# Convert from dictionary to series
result_series = pd.Series(d, index = ['e', 'b',
									'd', 'a',
									'c'])
# Print series
result_series
