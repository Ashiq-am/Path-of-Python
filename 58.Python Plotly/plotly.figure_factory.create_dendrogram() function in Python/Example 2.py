from plotly.figure_factory import create_dendrogram
import numpy as np


X = np.random.rand(5,5)
names = ['Jack', 'Oxana', 'John', 'Chelsea', 'Mark']

dendro = create_dendrogram(X, orientation='right', labels=names)
dendro.update_layout({'width':700, 'height':500})
dendro.show()
