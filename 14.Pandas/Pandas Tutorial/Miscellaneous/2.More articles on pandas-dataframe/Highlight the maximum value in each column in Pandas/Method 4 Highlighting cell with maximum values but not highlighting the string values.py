# Defining custom function which returns
# the list for df.style.apply() method
def highlight_max(s):
	if s.dtype == np.object:
		is_max = [False for _ in range(s.shape[0])]
	else:
		is_max = s == s.max()
	return ['background: lightgreen' if cell else '' for cell in is_max]

df.style.apply(highlight_max)
