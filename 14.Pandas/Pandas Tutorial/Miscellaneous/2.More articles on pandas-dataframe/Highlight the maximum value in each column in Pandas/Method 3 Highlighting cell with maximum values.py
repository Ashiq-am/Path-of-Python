# Defining custom function which returns
# the list for df.style.apply() method
def highlight_max(s):
	is_max = s == s.max()
	return ['background: lightgreen' if cell else '' for cell in is_max]

df.style.apply(highlight_max)
