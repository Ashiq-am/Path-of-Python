# function definition
def highlight_cols(s):
	color = 'red' if s < 6 else 'blue'
	return 'background-color: % s' % color

# highlighting the cells
display(df.style.applymap(highlight_cols))
