# Python program to demonstrate 3D scatter
# plot

import plotly.express as px

df = px.data.tips()

plot = px.scatter_3d(df, x = 'day',
					y = 'total_bill',
					z='sex')
plot.show()
