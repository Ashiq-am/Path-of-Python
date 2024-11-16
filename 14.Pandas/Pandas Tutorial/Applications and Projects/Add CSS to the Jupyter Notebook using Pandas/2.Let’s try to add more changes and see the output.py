from turtle import pd

df = pd.DataFrame({'A':[1, 2, 3, 4, 5, 6, 7, 8],
				'B':[1, 2, 3, 4, 5, 6, 7, 8],
				'C':[1, 2, 3, 4, 5, 6, 7, 8],
				'D':[1, 2, 3, 4, 5, 6, 7, 8],
				'E':[1, 2, 3, 4, 5, 6, 7, 8]})


df.style.set_table_styles(
[
{'selector': 'th',
'props': [('background', '# 606060'),
			('color', 'white'), ]},
{'selector': 'td',
'props': [('color', 'blue')]},
])
