import plotly.graph_objects as go

fig = go.Figure()

fig.add_trace(go.Barpolar(
	r=[10, 20, 30, 40],
	name='Wind 1',
))

fig.add_trace(go.Barpolar(
	r=[40, 20, 50, 10],
	name='Wind 2',
))

fig.show()
