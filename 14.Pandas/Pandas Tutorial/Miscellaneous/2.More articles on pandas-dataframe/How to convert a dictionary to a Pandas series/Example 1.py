# Import pandas library
import pandas as pd

# Create a dictionary
d = {'g' : 100, 'e' : 200,
	'k' : 400, 's' : 800,
	'n' : 1600}

# Convert from dictionary to series
result_series = pd.Series(d)

# Print series
result_series
