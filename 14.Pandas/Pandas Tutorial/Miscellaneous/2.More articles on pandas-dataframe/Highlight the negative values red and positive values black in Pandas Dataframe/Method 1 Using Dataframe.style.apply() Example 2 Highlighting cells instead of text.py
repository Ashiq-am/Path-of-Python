# Define a function which
# returns the list for
# df.style.apply() method
def highlight_max(s):
	if s.dtype == np.object:
		is_neg = [False for _ in range(s.shape[0])]
	else:
		is_neg = s < 0
	return ['background: red; color:white'
			if cell else 'background:black; color:white'
			for cell in is_neg]

# Using apply method of style
# attribute of Pandas DataFrame
df.style.apply(highlight_max)
