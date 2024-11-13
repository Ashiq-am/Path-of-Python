import plotly.graph_objects as go

feature_x = np.arange(0, 50, 2)
feature_y = np.arange(0, 50, 3)

# Creating 2-D grid of features
[X, Y] = np.meshgrid(feature_x, feature_y)

Z = np.cos(X / 2) + np.sin(Y / 4)

fig = go.Figure(data=go.Contour(
	x=feature_x, y=feature_y, z=Z,
	contours=dict(
		coloring='lines',
		showlabels=True,)
))

fig.show()
