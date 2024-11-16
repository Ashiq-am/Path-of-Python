# Define a function for
# colouring negative values
# red and positive values black
def highlight_max(cell):
	if type(cell) != str and cell < 0 :
		return 'color: red'
	else:
		return 'color: black'

df.style.applymap(highlight_max)
