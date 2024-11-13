import plotly.graph_objects as go

fig = go.Figure(data=go.Cone(x=[3],
							y=[1],
							z=[4],
							u=[1],
							v=[7],
							w=[2]))

fig.show()
