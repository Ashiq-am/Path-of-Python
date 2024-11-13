import plotly.graph_objects as go

fig = go.Figure(data=go.Cone(x=[1,3],
							y=[1,3],
							z=[1,4],
							u=[1,6],
							v=[1,7],
							w=[0,2]))

fig.show()
