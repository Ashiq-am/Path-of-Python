# importing the modules
import pandas as pd
import numpy as np

def color_negative_red(val):
	"""
	Takes a scalar and returns a string with
	the css property `'color: red'` for negative
	strings, black otherwise.
	"""
	color = 'blue' if val > 90 else 'black'
	return 'color: % s' % color

# creating a DataFrame
dict = {'Maths' : [87, 91, 97, 95],
		'Science' : [83, 99, 84, 76]}
df = pd.DataFrame(dict)

# displaying the DataFrame
df.style.applymap(color_negative_red)
