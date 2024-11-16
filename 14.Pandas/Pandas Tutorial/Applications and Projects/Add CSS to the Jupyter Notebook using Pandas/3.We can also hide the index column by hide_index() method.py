from pandas.tests.groupby.test_value_counts import df

df.style.set_table_styles(
[
{'selector': 'th',
'props': [('background', '# 606060'),
			('color', 'yellow'), ]},
{'selector': 'td',
'props': [('color', 'red')]},
]
).hide_index()
