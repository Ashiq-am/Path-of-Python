# iterating over color module
colorscale_names = []
colors_modules = ['carto', 'colorbrewer', 'cmocean', 'cyclical',
					'diverging', 'plotlyjs', 'qualitative', 'sequential']

for color_module in colors_modules:
	colorscale_names.extend([name for name, body
							in inspect.getmembers(getattr(px.colors, color_module))
							if isinstance(body, list)])
