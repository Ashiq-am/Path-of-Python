import pandas as pd

df = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})
df.to_html('write_html.html', index=False,
		border=3, justify='center')
