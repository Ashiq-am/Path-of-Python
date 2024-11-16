# Highlighting the maximum values
# of last 2 columns
df.style.highlight_max(subset = ['Age', 'Marks'],
					color = 'lightgreen', axis = 0)
