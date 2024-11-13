import plotly.graph_objects as go

fig = go.Figure()

fig.add_trace(go.Contourcarpet(
	a = [1, 2, 3, 4, 5, 6],
	b = [6, 5, 4, 3, 2, 1],
	z = [1, 1.96, 5, 6.1028, 4, 5.0625],
	autocontour = False,
	contours = dict(
		start = 1,
		end = 14,
		size = 1
	),
	line = dict(
		width = 2,
		smoothing = 0
	),
	colorbar = dict(
	len = 0.4,
		y = 0.25
	)
))


fig.add_trace(go.Carpet(
	a=[1, 2, 3, 4, 5, 6],
	b=[6, 5, 4, 3, 2, 1],
	y=[1, 2, 3, 4, 5, 6],

	aaxis=dict(
		tickprefix='F = ',
		ticksuffix='N',
		smoothing=0.2,
		minorgridcount=10,
	),
	baxis=dict(
		tickprefix='P = ',
		ticksuffix='pa',
		smoothing=0.4,
		minorgridcount=9,
	)
))

fig.show()
