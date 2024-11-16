# Define a function for colouring
# negative values red and
# positive values black
def highlight_max(s):
	if s.dtype == np.object:
		is_neg = [False for _ in range(s.shape[0])]
	else:
		is_neg = s < 0
	return ['color: red;' if cell else 'color:black'
			for cell in is_neg]

# Using apply method of style
# attribute of Pandas DataFrame
df.style.apply(highlight_max)
