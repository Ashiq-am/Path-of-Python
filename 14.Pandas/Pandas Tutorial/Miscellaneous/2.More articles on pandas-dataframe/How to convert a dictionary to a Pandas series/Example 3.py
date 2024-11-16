# Import pandas library
import pandas as pd

# Create a dictionary
d = {'a' : 10, 'b' : 20,
	'c' : 40, 'd':80}

# Convert from dictionary to series
result_series = pd.Series(d, index = ['b', 'd',
									'e', 'a',
									'c'])
# Print series
result_series
