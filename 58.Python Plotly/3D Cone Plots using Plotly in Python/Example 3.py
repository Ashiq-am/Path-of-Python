import plotly.graph_objects as go

fig = go.Figure(data=go.Cone(x=[11,31, 12],
							y=[12,32, 21],
							z=[13,41, 15],
							u=[14,16, 17],
							v=[15,27, 10],
							w=[10,29, 21]))

fig.show()
