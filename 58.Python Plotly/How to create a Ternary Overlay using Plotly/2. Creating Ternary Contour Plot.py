import plotly.express as px
import plotly.graph_objects as go


df = px.data.iris()
fig = go.Figure(go.Scatterternary({
	'mode': 'lines',
	'a': df['sepal_length'],
	'b': df['sepal_width'],
	'c': df['petal_length'],
	'line': {'color': '#444', 'shape': 'spline'},
	'marker': {
		'color': 'green',
		'size': 14,
		'line': {'width': 2}
	}
}))

fig.show()