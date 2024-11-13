from plotly.subplots import make_subplots
import plotly.graph_objects as go
from plotly import offline

fig = make_subplots(rows=2, cols=2)

fig.add_trace(go.Scatter(x=[20, 30, 40], y=[50, 60, 70],
						name="2017", legendgroup="2017",
						line=dict(color='blue')),
			row=1, col=1)

fig.add_trace(go.Scatter(x=[20, 30, 40], y=[50, 60, 60],
						name="2018", legendgroup="2018",
						line=dict(color='red')),
			row=1, col=1)


fig.add_trace(go.Scatter(x=[10, 20, 30], y=[20, 25, 30],
						name="2017", legendgroup="2017",
						line=dict(color='blue'),
						showlegend=False
						),
			row=1, col=2)

fig.append_trace(go.Scatter(x=[20, 30, 40], y=[50, 60, 70],
							name="2018", legendgroup="2018",
							line=dict(color='yellow'),
							showlegend=True),
				row=1, col=2)

fig.append_trace(go.Scatter(x=[20, 30, 40], y=[50, 60, 70],
							name="2018", legendgroup="2018",
							line=dict(color='red'),
							showlegend=False),
				row=2, col=1)


fig.add_trace(go.Scatter(x=[10, 20, 30], y=[20, 25, 30],
						name="2017", legendgroup="2017",
						line=dict(color='pink'),
						showlegend=True
						),
			row=2, col=2)


fig.update_layout(height=600, width=600,
				title_text="Stacked Subplots")
fig.show()
