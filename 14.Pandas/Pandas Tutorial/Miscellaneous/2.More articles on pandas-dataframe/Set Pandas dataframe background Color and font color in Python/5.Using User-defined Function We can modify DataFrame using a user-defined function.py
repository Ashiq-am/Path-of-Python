# function for set text color of positive
# values in Dataframes
def color_positive_green(val):
	"""
	Takes a scalar and returns a string with
	the css property `'color: green'` for positive
	strings, black otherwise.
	"""
	if val > 0:
		color = 'green'
	else:
		color = 'black'
	return 'color: %s' % color

df.style.applymap(color_positive_green)
