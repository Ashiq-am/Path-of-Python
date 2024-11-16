# Using dataframe.xs() function
# to get values at several indexes
# and levels
df.xs(('Birds', 'flies'),
	level=[0, 'locomotion'])
