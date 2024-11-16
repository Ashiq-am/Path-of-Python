# converting data into wide-format
data_wide = df.pivot(columns='continent',
					values='lifeExp')
data_wide.head()
