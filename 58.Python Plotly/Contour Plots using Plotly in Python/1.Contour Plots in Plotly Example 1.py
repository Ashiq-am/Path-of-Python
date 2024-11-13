import plotly.graph_objects as go
import numpy as np

data = [[1,2,3,4,5],
	[3,4,5,6,7],
	[7,8,9,6,4],
	[3,7,2,4,2]]

fig = go.Figure(data =
	go.Contour(z = data))

fig.show()
