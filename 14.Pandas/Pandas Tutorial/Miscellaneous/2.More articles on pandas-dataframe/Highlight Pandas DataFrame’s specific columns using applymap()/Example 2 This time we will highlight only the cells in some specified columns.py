# function definition
def highlight_cols(s):
	return 'background-color: % s' % 'yellow'

# highlighting the cells
display(df.style.applymap(highlight_cols,
						subset = pd.IndexSlice[:, ['B', 'C']]))
