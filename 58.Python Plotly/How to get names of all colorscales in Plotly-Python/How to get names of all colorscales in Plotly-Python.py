# import the modules
import inspect
import plotly.express as px
from textwrap import fill

# iterating over color module
colorscale_names = []
colors_modules = ['carto', 'cmocean', 'cyclical',
					'diverging', 'plotlyjs', 'qualitative', 'sequential']
for color_module in colors_modules:
	colorscale_names.extend([name for name, body
							in inspect.getmembers(getattr(px.colors, color_module))
							if isinstance(body, list)])


print(fill(''.join(sorted({f'{x: <{15}}' for x in colorscale_names})), 75))
