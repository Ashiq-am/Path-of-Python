import pandas as pd
import plotly.offline as py
import plotly.graph_objs as go
import cufflinks as cf
cf.go_offline()

df = pd.DataFrame(data=[[2, 3, 4], [8, 27, 64]],
				columns=['A', 'B', 'C'])

# get figure property
fig = df.iplot(kind='scatter', asFigure=True)

# set layout_showlegend=False
fig.update(layout_showlegend=False)

# generate webpage
py.plot(fig)
