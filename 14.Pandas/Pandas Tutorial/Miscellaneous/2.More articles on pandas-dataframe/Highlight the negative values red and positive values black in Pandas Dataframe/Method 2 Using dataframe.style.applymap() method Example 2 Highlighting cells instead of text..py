# Define a function which
# returns string for
# applymap() method
def highlight_max(cell):
	if type(cell) != str and cell < 0 :
		return 'background: red; color:black'
	else:
		return 'background: black; color: white'

df.style.applymap(highlight_max)
