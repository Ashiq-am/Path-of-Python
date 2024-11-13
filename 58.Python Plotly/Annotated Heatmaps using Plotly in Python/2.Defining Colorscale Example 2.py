import plotly.figure_factory as ff
import numpy as np

feature_x = np.arange(0, 10, 2)
feature_y = np.arange(0, 10, 3)

# Creating 2-D grid of features
[X, Y] = np.meshgrid(feature_x, feature_y)

Z = np.cos(X / 2) + np.sin(Y / 4)

custom = [[0, 'green'], [0.5, 'red']]

fig = ff.create_annotated_heatmap(Z, colorscale=custom)
fig.show()
