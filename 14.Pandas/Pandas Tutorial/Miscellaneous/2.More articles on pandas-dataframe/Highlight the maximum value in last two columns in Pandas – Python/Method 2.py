# Highlighting the maximum values of
# last 2 columns
df.style.highlight_max(subset = df.columns[-2:],
					color = 'lightgreen', axis = 0)
