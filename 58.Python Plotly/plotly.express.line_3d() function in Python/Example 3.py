# Python program to demonstrate scatter
# plot

import plotly.express as px

df = px.data.tips()

plot = px.line_3d(df, x = 'day',
					y = 'total_bill',
					z = 'sex',
					color = 'time',
					line_group = 'sex')
plot.show()