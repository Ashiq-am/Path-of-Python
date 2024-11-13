# Python program to demonstrate scatter
# plot

import plotly.express as px

df = px.data.tips()

plot = px.scatter(df, x = 'day',
				y = 'total_bill',
				color='sex')
plot.show()
