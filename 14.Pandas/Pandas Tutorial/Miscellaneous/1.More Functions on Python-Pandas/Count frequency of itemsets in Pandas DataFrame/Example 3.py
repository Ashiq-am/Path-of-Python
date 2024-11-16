import pandas as pd

df = pd.DataFrame({
	'A': ['Box', 'Color', 'Pencil', 'Eraser',
		'Color', 'Pencil', 'Eraser', 'Color',
		'Color', 'Eraser', 'Eraser', 'Pencil'],

	'B': ['Jammu', 'Kolkata', 'Bihar', 'Gujrat',
		'Kolkata', 'Bihar', 'Jammu', 'Bihar',
		'Gujrat', 'Jammu', 'Kolkata', 'Bihar']
})


freq = df.groupby(['A'])['B'].agg('count').reset_index()
display(freq)

freq = df.groupby(['B'])['A'].agg('count').reset_index()
display(freq)
