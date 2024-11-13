import pandas as pd
import plotly.offline as py
import plotly.graph_objs as go
import cufflinks as cf
cf.go_offline()

df = pd.DataFrame(data=[[2, 3, 4], [8, 27, 64]],
				columns=['A', 'B', 'C'])

# get figure property
fig = df.iplot(kind='scatter', asFigure=True)

# set showlegend property by name of trace
for trace in fig['data']:
	if(trace['name'] != 'B'):
		trace['showlegend'] = False

# generate webpage
py.plot(fig)
