import pandas as pd

df = pd.DataFrame({
	'A': ['Box', 'Color', 'Pencil', 'Eraser',
		'Color', 'Pencil', 'Eraser', 'Color',
		'Color', 'Eraser', 'Eraser', 'Pencil'],

	'B': ['Jammu', 'Kolkata', 'Bihar', 'Gujrat',
		'Kolkata', 'Bihar', 'Jammu', 'Bihar',
		'Gujrat', 'Jammu', 'Kolkata', 'Bihar']
})

count = df['A'].value_counts()
display(count)

count = df['B'].value_counts()
display(count)
