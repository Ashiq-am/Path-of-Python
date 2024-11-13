from plotly.figure_factory import create_dendrogram
import numpy as np


X = np.random.rand(10,10)
fig = create_dendrogram(X)
fig.show()
