import plotly.graph_objects as go

fig = go.Figure(data=go.Streamtube(x=[1, 1, 1], y=[1, 1, 2],
								z=[0, 0, 0], u=[0, 0, 0],
								v=[1, 1, 1], w=[0, 0, 0]))
fig.show()
